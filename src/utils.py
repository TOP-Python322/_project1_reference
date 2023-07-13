"""
Вспомогательный модуль: вспомогательные функции.
"""

# стандартная библиотека
from configparser import ConfigParser
from pprint import pprint
# проект
import data


def read_players() -> bool:
    """"""
    cp = ConfigParser()
    cp.read(data.PLAYERS_DB_PATH)
    for player in cp.sections():
        data.players_db[player] = {
            k: int(v)
            for k, v in cp[player].items()
        }
    return bool(data.players_db)

