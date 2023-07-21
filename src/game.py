"""
Основной модуль: настройка игры и игровой процесс.
"""

# стандартная библиотека
from shutil import get_terminal_size
# проект
import bot
import data
import utils


def mode():
    ...
    # if bot_name == '#1'
    #     data.bot_level = bot.easy

    # if bot_name == '#2'
    #     data.bot_level = bot.hard


def load():
    ...


def game() -> list[str] | None:
    """Контроллер игрового процесса.
    
    Возвращает список имён в формате ['имя_выигравшего', 'имя_проигравшего'], пустой список для ничьей или None, если партия не завершена.
    """
    # 10. Цикл до максимального количества ходов
    for t in range(len(data.turns), data.all_cells):
        # индекс-указатель на игрока и токен
        parity = t % 2
        
        # шаги 11–13
        ...
    else:
        utils.header_text('ничья', level=2)
        return []


def get_human_turn() -> int | None:
    """"""
    while True:
        turn = input(data.MESSAGES['ввод хода'])
        if turn:
            try:
                turn = int(turn)
            except ValueError:
                print(data.MESSAGES['ход не число'])
            else:
                if 0 <= turn < data.all_cells:
                    if turn not in data.turns:
                        return turn
                    else:
                        print(data.MESSAGES['ход в занятую'])
                else:
                    print(data.MESSAGES['ход не в диапазоне'])
        else:
            return None


def save():
    ...


def print_board(token_index: int = 0) -> None:
    """"""
    board = tuple((data.board | data.turns).values())
    board = data.field.format(*board)
    
    if data.DEBUG:
        for vector in data.debug_data.values():
            max_width = max(len(str(n)) for n in vector)
            templ = utils.field_template(max_width)
            vector = templ.format(*(f'{n:^{max_width}}' for n in vector))
            if token_index:
                board = utils.concatenate_lines(vector, board, padding=5)
            else:
                board = utils.concatenate_lines(board, vector, padding=5)
    
    if token_index:
        term_width = get_terminal_size()[0] - 1
        board_width = len(board.split('\n', 1)[0])
        margin = ' '*(term_width - board_width)
        margin = '\n'.join([margin]*(2*data.dim-1))
        board = utils.concatenate_lines(margin, board, padding=0)
    
    print(board)



def check_win():
    ...

