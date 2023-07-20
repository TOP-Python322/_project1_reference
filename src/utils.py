"""
Вспомогательный модуль: вспомогательные функции.
"""

# стандартная библиотека
from configparser import ConfigParser
from shutil import get_terminal_size
from typing import Literal
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
        multiline1: str,
        multiline2: str,
        *multilines: str,
        padding: int = 8
) -> str:
    """Принимает на вход мнострочные объекты str и возвращает один объект str, строчки которого составлены из соответствующих строчек каждого переданного объекта, раздёлнных отступом."""
    multilines = multiline1, multiline2, *multilines
    multilines = [m.split('\n') for m in multilines]
    padding = ' '*padding
    return '\n'.join(
        padding.join(row)
        for row in zip(*multilines)
    )


# >>> board1 = field_template().format(*['X']*9)
# >>> board2 = field_template().format(*['O']*9)
# >>>
# >>> print(concatenate_lines(board1, board2))
#  X | X | X          O | O | O
# ———————————        ———————————
#  X | X | X          O | O | O
# ———————————        ———————————
#  X | X | X          O | O | O


def clear() -> None:
    """"""
    data.active_players = [data.authorized_player]
    data.turns = {}


def header_text(
        text: str, 
        *, 
        level: Literal[1, 2, ...], 
        v_fill: str = '#', 
        h_fill: str = '='
) -> str:
    """Возвращает переданную строку, форматированную как заголовок. Форматирование отличается для разных уровней заголовка. Также могут быть изменены символы-заполнители."""
    term_width = get_terminal_size()[0] - 1
    data_width = term_width - 12
    text_len = len(text)
    
    if level == 1:
        text = text.upper()
        edge = v_fill + h_fill*(term_width-2) + v_fill
        padding = v_fill + ' '*(term_width-2) + v_fill
        text = '\n'.join(
            v_fill + line.center(term_width-2) + v_fill
            for line in columnize(text, term_width-6)
        )
        return f'{edge}\n{padding}\n{text}\n{padding}\n{edge}'
    
    elif level == 2:
        text = text.upper()
        if text_len <= data_width:
            return f'  {text}  '.center(term_width, h_fill)
        else:
            return '\n'.join(
                h_fill*4 + line.center(data_width+4) + h_fill*4
                for line in columnize(text, data_width)
            )
    
    # elif level == 3:
    #     ...
    
    else:
        raise ValueError


def columnize(text: str, column_width: int) -> list[str]:
    """Разбивает переданную строку на отдельные слова и формирует из слов строки, длины которых не превышают заданное значение. Возвращает список строк, к которым впоследствии может быть применено любое выравнивание."""
    multiline, line_len, i = [[]], 0, 0
    for word in text.split():
        word_len = len(word)
        if line_len + word_len + len(multiline[i]) <= column_width:
            multiline[i] += [word]
            line_len += word_len
        else:
            multiline += [[word]]
            line_len = word_len
            i += 1
    return [' '.join(line) for line in multiline]


# >>> print(header_text(data.APP_TITLE, level=1))
# #=============================================================================#
# #                                                                             #
# #                               КРЕСТИКИ-НОЛИКИ                               #
# #                                                                             #
# #=============================================================================#
# >>> 
# >>> print(header_text('победил Игрок1', level=2))
# ===============================  ПОБЕДИЛ ИГРОК1  ==============================
# >>>
# >>> text = '''по результатам финальной турнирной схватки на огромном поле 20х20 побеждает игрок с псведонимом Снайпер'''
# >>>
# >>> print(header_text(text, level=2))
# ====   ПО РЕЗУЛЬТАТАМ ФИНАЛЬНОЙ ТУРНИРНОЙ СХВАТКИ НА ОГРОМНОМ ПОЛЕ 20Х20   ====
# ====                 ПОБЕЖДАЕТ ИГРОК С ПСВЕДОНИМОМ СНАЙПЕР                 ====

