#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dnf install librsvg2-tools
# apt install librsvg2-bin

import hashlib
import os
import sys
import logging
import re
from pathlib import Path, PurePath  # nueva forma de trabajar con rutas
from typing import Dict, Text, NoReturn, List

import pypandoc

from implement_sqlite import select_all_hashes, insert_file, update_file, check_database
from file import File
from procamora_utils.logger import get_logging

log: logging = get_logging(False, 'generate_pdf')

WORK: Path = Path(__file__).resolve().parent.parent
WORK_CONTENT: Path = Path(WORK, 'content/post')
WORK_IMAGES: Path = Path(WORK, 'static')
log.info(WORK)


def get_hashsum(file: Path) -> Text:
    # https://nitratine.net/blog/post/how-to-hash-files-in-python/
    BLOCK_SIZE: int = 65536  # The size of each read from the file (4096 *16) 16 paginas de usuario

    file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(str(file), 'rb') as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    # print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash
    return file_hash.hexdigest()


def add_absolute_path_images(file: Path) -> Text:
    regex: Text = r'(/images/.*)'
    log.warning(WORK_IMAGES)
    return re.sub(regex, rf'{WORK_IMAGES}\1', file.read_text())


def generate_pdf(file: Path) -> bool:
    dirpath_pdf: Path = Path(WORK, 'static', 'pdf')
    file_pdf: Path = Path(dirpath_pdf, f'{str(file.name)[0:-3]}.pdf')  # elimino .md [0:-3]

    if not dirpath_pdf.exists():
        log.debug(f'Create directory: {dirpath_pdf}')
        dirpath_pdf.mkdir()

    log.info(f'Generate PDF: {file_pdf}')
    try:
        file_path: Text = add_absolute_path_images(file)
        # log.warning(file_path)
        output: Text = pypandoc.convert_text(source=file_path, to='pdf', format='md', outputfile=str(file_pdf),
                                             extra_args=['-V', 'geometry:margin=1.5cm',
                                                         # '--pdf-engine=xelatex'
                                                         # wkhtmltopdf, weasyprint, pagedjs-cli, prince, pdflatex, lualatex, xelatex, latexmk, tectonic, pdfroff, context
                                                         '--pdf-engine=xelatex'
                                                         ])
        assert output == ""
        return True
    except RuntimeError as e:
        log.error(f'{file} -> {e}')
        # Si falla el modo bueno se hace con otro que continua pese a no tener las imagenes
        return False


def main() -> NoReturn:
    # Obtengo recurisvamente todos los ficheros .md
    if not WORK_CONTENT.exists():
        log.error(f'[*] No exit: {WORK_CONTENT}')
        sys.exit(1)

    files: List[Path] = list(WORK_CONTENT.rglob("*.md"))
    if len(files) == 0:
        log.warning(f'[*] No detect files in {WORK_CONTENT}')

    check_database()
    all_hashes: Dict[str, File] = select_all_hashes()

    for f in files:
        if not re.search('buscar-y-remplazar.md', str(f)):
            continue
        file: Text = str(f)
        file_hash: Text = get_hashsum(f)
        # Si el fichero no existe se inserta en la BD
        if not file in all_hashes.keys():
            insert_file(file, file_hash)
            generate_pdf(f)
        # Si el fichero existe comprobamos que tiene el mismo hash
        elif all_hashes[file].shasum != file_hash:
            log.info(f'{all_hashes[file]} != {file_hash}')
            update_file(file, file_hash)
            generate_pdf(f)

    log.info('Finished')


if __name__ == '__main__':
    main()
