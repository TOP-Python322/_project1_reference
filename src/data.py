"""
Вспомогательный модуль: глобальные переменные и условные константы.
"""

# стандартная библиотека
from pathlib import Path
from re import compile
from sys import path


APP_TITLE = 'КРЕСТИКИ-НОЛИКИ'

ROOT_DIR = Path(path[0]).parent
PLAYERS_DB_PATH = ROOT_DIR / 'data/players.ini'
SAVES_DB_PATH = ROOT_DIR / 'data/saves'

name_pattern = compile(r'[a-zA-Zа-яА-Я][а-яА-Я\w]+')
dim_pattern = compile(r'[3-9]|1\d|20')

# база игроков - имена и статистика игроков 
players_db: dict[str, dict[str, int]] = {}


COMMANDS = {
    'помощь': ('help', 'помощь'),
    'новая партия': ('new', 'игра'),
    'загрузка': ('load', 'загрузка'),
    'авторизация': ('player', 'игрок'),
    'статистика': ('table', 'таблица'),
    'размер поля': ('dim', 'размер'),
    'выход': ('quit', 'выход'),
}


authorized_player: str = None
active_players: list[str] = []

TOKENS = ('X', 'O')

dim: int = 3
dim_range: range = range(dim)
all_cells: int = dim**2

field: str = None

board: dict[int, str] = dict.fromkeys(range(all_cells), ' ')
turns: dict[int, str] = {}


MESSAGES = {
    'ввод команды': '\n _ введите команду: ',
    'ввод имени': '\n _ введите имя: ',
    'некорректное имя': ' ! имя игрока должно начинаться с буквы и быть не короче двух символов',
    'ввод размера': '\n _ введите новый размер игрового поля: ',
    'некорректный размер': ' ! размер должен быть введён числом от 3 до 20',
    'ввод хода': '\n _ введите номер свободной ячейки: ',
    'ход не число': ' ! номер ячейки должен быть числом',
    'ход не в диапазоне': f' ! номер ячейки должен находиться в диапазоне от 0 до {all_cells-1} включительно',
    'ход в занятую': ' ! ячейка занята',
    # '': '',
}

