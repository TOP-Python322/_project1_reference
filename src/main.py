"""
Главный модуль: точка входа.
"""

# проект
import data
import game
import help
import players
import utils

# 1. Чтение файлов данных
# 2. ЕСЛИ первый запуск:
if utils.read_players():
    # вывод раздела помощи 
    help.show_help()

# 3. Запрос имени игрока
players.get_player()

# суперцикл (главное меню)
while True:
    # 4. Ожидание ввода команды игрока
    command = input(data.PROMPT)
    
    if command in data.COMMANDS['новая партия']:
        game.mode()
        result = game.game()
        if result:
            players.update()
    
    # elif command in data.COMMANDS['']:
    
    elif command in data.COMMANDS['выход']:
        break

# 20. Действия перед завершением работы приложения
