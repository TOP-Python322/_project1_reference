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


def concatenate_lines(
        matrix1: str,
        matrix2: str,
        *matrices: str,
        padding: int = 8
) -> str:
    """Принимает на вход мнострочные объекты str и возвращает один объект str, строчки которого составлены из соответствующих строчек каждого переданного объекта, раздёлнных отступом."""
    matrices = matrix1, matrix2, *matrices
    matrices = [m.split('\n') for m in matrices]
    padding = ' '*padding
    return '\n'.join(
        padding.join(row)
        for row in zip(*matrices)
    )


