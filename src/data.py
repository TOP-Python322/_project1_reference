"""
Вспомогательный модуль: глобальные переменные и условные константы.
"""

# стандартная библиотека
from pathlib import Path
from sys import path


ROOT_DIR = Path(path[0]).parent
PLAYERS_DB_PATH = ROOT_DIR / 'data/players.ini'
SAVES_DB_PATH = ROOT_DIR / 'data/saves'


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


