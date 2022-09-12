#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from pathlib import Path  # nueva forma de trabajar con rutas
from typing import List, Text, NoReturn, Tuple, Dict, Any

from procamora_utils.interface_sqlite import conection_sqlite, execute_script_sqlite
from procamora_utils.logger import get_logging

from file import File

logger: logging = get_logging(False, 'sqlite')


# Ruta absoluta de la BD
DB: Path = Path(Path(__file__).resolve().parent, "wiki.db")
DB_STRUCTURE: Path = Path(Path(__file__).resolve().parent, "wiki.db.sql")

def check_database() -> NoReturn:
    """
    Comprueba si existe la base de datos, sino existe la crea
    :return:
    """
    try:
        query: Text = "SELECT * FROM Hosts"
        conection_sqlite(DB, query)
    except OSError:
        logger.info(f'the database {DB} doesn\'t exist, creating it with the default configuration')
        execute_script_sqlite(DB, DB_STRUCTURE.read_text())


def select_all_hashes() -> Dict[Text, File]:
    query: Text = "SELECT * FROM hashes"
    response_query: List[Dict[Text, Any]] = conection_sqlite(DB, query, is_dict=True)
    response: Dict[Text, File] = dict()
    for i in response_query:
        file: File = File(i['id'], i['file'], i['hash'])
        response[file.file] = file
    return response


def insert_file(file: Text, hash: Text) -> NoReturn:
    query: Text = f"INSERT INTO hashes(file, hash) VALUES ('{file}','{hash}');"
    logger.debug(query)
    conection_sqlite(DB, query)


def update_file(file: Text, hash: Text) -> NoReturn:
    query: Text = f"UPDATE hashes SET hash='{hash}' WHERE file LIKE '{file}';"
    logger.debug(query)
    conection_sqlite(DB, query)
