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
    if data.authorized_player is None:
        data.authorized_player = name
    data.active_players += [name]
    utils.write_players()


def update(names: list[str]) -> None:
    """"""
    if names:
        winner, looser = names
        # AFNP (Ask Forgivness, Not Permission — лучше просить прощения, чем разрешения) — имеет смысл, если исключение KeyError возникает редко, то есть в winner и looser редко оказывается имя бота
        try:
            data.players_db[winner]['wins'] += 1
        except KeyError:
            pass
        try:
            data.players_db[looser]['fails'] += 1
        except KeyError:
            pass
    else:
        for name in data.active_players:
            # логическое выражение выполняется всегда — чтобы оправдать его выполнение, необходимо понять, насколько часто в name действительно оказывается имя бота
            if not name.startswith('#'):
                data.players_db[name]['ties'] += 1

