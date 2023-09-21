#!/share/CACHEDEV1_DATA/.qpkg/Python3/python3/bin/python3
# -*- coding: <utf8> -*-

# /share/CACHEDEV1_DATA/.qpkg/Python3/python3/bin/python3 -m pip install procamora_utils humanize

from typing import List, Text, Tuple, Dict
from pathlib import Path
import re
import os
import logging
from procamora_utils.logger import get_logging
import humanize

log: logging = get_logging(False, 'movies')

regex_movies = r'\.(mkv|avi|mp4)$'


def get_files_recursive(directory: Path) -> Tuple[List[Path], List[Path], List[Path]]:
    log.info('[+] searching all files')
    all_movies: List[Path] = list(directory.rglob('*'))

    log.info('[+] searching all files skiped')
    movies_skip: List[Path] = list(filter(
        lambda x: x.is_file() and not re.search(regex_movies, x.name, re.IGNORECASE) and
                  not re.search(r'\.md$', x.name, re.IGNORECASE), all_movies))
    # if len(movies_skip)>0:
    m = '\n\t'.join([str(m) for m in movies_skip])
    log.warning(f'[*] skip {len(movies_skip)} movies:\n\t{m}')

    log.info('[+] searching all movies')
    movies: List[Path] = list(filter(
        lambda x: x.is_file() and re.search(regex_movies, x.name, re.IGNORECASE), all_movies))

    log.info('[+] searching all movies no imdb')
    no_imdbid: List[Path] = list(filter(
        lambda x: not re.search(r'\[imdbid-tt\d+\]', x.name, re.IGNORECASE), movies))
    return all_movies, movies, no_imdbid


def write_no_imdb(movies: List[Path], filename: Path) -> None:
    no_imdb_movies: List[Text] = [str(m) for m in movies]
    m = '\n\t'.join(no_imdb_movies)
    log.warning(f'[*] no_imdb_movies {len(no_imdb_movies)} movies:\n\t{m}')
    filename.write_text('\n'.join(no_imdb_movies))


def write_sorted_files(movies: List[Path], filename: Path) -> None:
    movies_name: List[Text] = []
    list(map(lambda x: movies_name.append(x.name), movies))  # movies_name = [movie.name for movie in movies]
    movies_name.sort()

    filename.write_text('\n'.join(movies_name))


def write_files_sizes(files: List[Path], filename: Path) -> None:
    movies_sizes: List[Tuple[Text, float]] = [(file.name, os.path.getsize(file)) for file in files]
    movies_sizes_sorted: List[Tuple[Text, float]] = sorted(movies_sizes, key=lambda x: x[1], reverse=True)
    movies_human_sizes_sorted: List[Tuple[Text, Text]] = list(
        map(lambda m: (m[0], humanize.naturalsize(m[1])), movies_sizes_sorted))

    log.debug(movies_human_sizes_sorted)

    filename.write_text('\n'.join(map(lambda x: f'{x[1]} - {x[0]}', movies_human_sizes_sorted)))


def find_duplicate_files(movies):
    log.info('[+] searching duplicates')
    file_dict: Dict[Text, List[Text]] = {}  # movies name duplicate
    file_dict_imdb: Dict[Text, List[Text]] = {}  # movies imdbid  duplicate

    for path in movies:
        # Obtener el nombre del archivo y la ubicación
        file_name_clean = re.sub(r'\[(.*?)\]|\((.*?)\)|-(.*?)|(\.(mkv|avi|mp4)$)', '', path.name).strip()
        imdbid_match: re.Match = re.search(r"(imdbid-tt\d+)", path.name)
        imdbid = imdbid_match.group(0) if imdbid_match else ""
        file_name = f'{file_name_clean.lower()} [{imdbid}]'
        file_path = str(path)

        # Agregar el archivo a la lista de ubicaciones si la clave ya existe
        if file_name in file_dict:
            file_dict[file_name].append(file_path)
        # Agregar la clave y la primera ubicación si la clave no existe
        else:
            file_dict[file_name] = [file_path]

        # Agregar el archivo a la lista de ubicaciones si la clave ya existe
        if imdbid in file_dict_imdb:
            file_dict_imdb[imdbid].append(file_path)
        # Agregar la clave y la primera ubicación si la clave no existe
        else:
            file_dict_imdb[imdbid] = [file_path]

    # Imprimir los archivos que se encontraron en múltiples ubicaciones
    log.info(f"[+] search duplicates name")
    duplicates: bool = False
    for file_name, file_paths in file_dict.items():
        if len(file_paths) > 1:
            duplicates = True
            m = '\n\t'.join(file_paths)
            log.warning(f"[*] '{file_name}' se encontró en las siguientes ubicaciones:\n\t{m}")

    if not duplicates:
        log.info(f"[+] no duplicates name")

    log.info(f"[+] search duplicates imdb")
    duplicates_imdb: bool = False
    for imdbid, file_paths in file_dict_imdb.items():
        if imdbid == '':  # is no imdb not duplicate
            continue
        # print(imdbid)
        # print(file_paths)
        if len(file_paths) > 1:
            duplicates_imdb = True
            m = '\n\t'.join(file_paths)
            log.warning(f"[*] '{imdbid}' se encontró en las siguientes ubicaciones:\n\t{m}")

    if not duplicates_imdb:
        log.info(f"[+] no duplicates imdbid")


def main():
    # Ejemplo de uso
    directory = Path("/Users/pablojoserocamora/qnap/MyMovies")

    movies: List[Path]
    #all_movies: List[Path]
    no_imdbid: List[Path]
    _, movies, no_imdbid = get_files_recursive(directory)

    # if len(no_imdbid) > 0:
    write_no_imdb(no_imdbid, Path("movies_no_imdb.txt"))

    write_sorted_files(movies, Path("movies_sorted.txt"))
    write_files_sizes(movies, Path("movies_sorted_sized.txt"))
    find_duplicate_files(movies)


if __name__ == '__main__':
    main()
