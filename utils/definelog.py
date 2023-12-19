import platform
import logging
import os
from typing_extensions import Literal
from pathlib import Path


class Logger:
    def __init__(self, log_path: Path) -> None:
        self.log_path: Path = log_path

    def define_logger(self,
                      fmt: str = '%(asctime)s %(name)s %(levelname)s \t %(message)s',
                      datefmt: str = '%Y-%m-%d %H:%M:%S',
                      ) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        file_handler = logging.FileHandler(filename=self.log_path, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    @staticmethod
    def basic_fill(lang: Literal['pl', 'eng'] = 'eng') -> None:
        host: str = platform.node()
        platforma: str = platform.platform()
        python_version: str = platform.python_version()
        username: str = os.environ['USER']
        work_dir: str = os.getcwd()
        if lang == 'pl':
            logging.info(f'Host: {host}')
            logging.info(f'Platforma: {platforma}')
            logging.info(f'Wersja Python\'a: {python_version}')
            logging.info(f'Nazwa użytkownika: {username}')
            logging.info(f'Katalog projektu: {work_dir}')
            logging.info('')
            logging.info('-- ROZPOCZĘCIE --')
        elif lang == 'eng':
            logging.info(f'Host: {host}')
            logging.info(f'Platform: {platforma}')
            logging.info(f'Python version: {python_version}')
            logging.info(f'User: {username}')
            logging.info(f'Project path: {work_dir}')
            logging.info('')
            logging.info('-- START --')
