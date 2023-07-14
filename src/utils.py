"""
Вспомогательный модуль: вспомогательные функции.
"""

# стандартная библиотека
from configparser import ConfigParser
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


def write_players() -> None:
    """"""
    cp = ConfigParser()
    cp.read_dict(data.players_db)
    with open(data.PLAYERS_DB_PATH, 'w', encoding='utf-8') as fileout:
        cp.write(fileout)


def field_template(width: int = 1) -> str:
    """"""
    row = '|'.join([' {} ']*data.dim)
    h_line = '—'*(data.dim*(width+2) + data.dim-1)
    return f'\n{h_line}\n'.join([row]*data.dim)

