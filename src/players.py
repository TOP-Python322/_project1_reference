"""
Основной модуль: взаимодействие с игроками.
"""

# проект
import data
import utils


def get_name() -> None:
    """"""
    while True:
        name = input(data.MESSAGES['ввод имени'])
        if data.name_pattern.fullmatch(name):
            break
        print(data.MESSAGES['некорректное имя'])
    if name not in data.players_db:
        data.players_db[name] = {
            'wins': 0,
            'fails': 0,
            'ties': 0
        }
    utils.write_players()

