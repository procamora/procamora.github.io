#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import sys
from pathlib import Path  # nueva forma de trabajar con rutas
from threading import Lock
from typing import Dict, Any, List, Union, Tuple, Optional, Text, NoReturn

from file import File
from logger import get_logger

logger = get_logger(True, 'sqlite')
DB = "wiki.db"


def conection_sqlite(db: Text, query: Text, mutex: Lock = None, is_dict: bool = False) \
        -> Union[List[Dict[Text, Any]], None]:
    if mutex is not None:
        mutex.acquire()  # bloqueamos acceso a db
    try:
        if os.path.exists(db):
            conn = sqlite3.connect(db)
            if is_dict:
                conn.row_factory = dict_factory
            cursor = conn.cursor()
            cursor.execute(query)

            if query.upper().startswith('SELECT'):
                data = cursor.fetchall()  # Traer los resultados de un select
            else:
                conn.commit()  # Hacer efectiva la escritura de datos
                data = None

            cursor.close()
            conn.close()
            return data
        else:
            logger.critical(f'Database {DB} not exits')
            sys.exit(-1)
    except sqlite3.OperationalError:
        logger.critical(f'LOCK {query}, sorry...')
    finally:
        if mutex is not None:
            mutex.release()  # liberamos mutex


def dict_factory(cursor: sqlite3.Cursor, row: Tuple[Text]) -> Dict[Text, Text]:
    d: Dict = dict()
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def execute_script_sqlite(database: Path, script: Text) -> None:
    conn = sqlite3.connect(str(database))
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    cursor.close()
    conn.close()


def dump_database(database: Path) -> Optional[Text]:
    """
    Hace un dump de la base de datos y lo retorna
    :param database: ruta de la base de datos
    :return dump: volcado de la base de datos
    """
    if database.exists():
        con = sqlite3.connect(str(database))
        a: Text = '\n'.join(con.iterdump())
        return str(a)
    return None


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
