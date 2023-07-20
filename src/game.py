"""
Основной модуль: настройка игры и игровой процесс.
"""

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
    data.field = utils.field_template()
    # 10. Цикл до максимального количества ходов
    for t in range(len(data.turns), data.all_cells):
        # индекс-указатель на игрока и токен
        parity = t % 2
        
        # шаги 11–13
        ...
    else:
        utils.header_text('ничья', level=2)
        return []


def get_human_turn():
    ...


def save():
    ...


def print_board():
    ...


def check_win():
    ...

