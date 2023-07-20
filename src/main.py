"""
Главный модуль: точка входа.
"""

# проект
import data
import game
import help
import players
import utils


utils.header_text(data.APP_TITLE, level=1)

# 1. Чтение файлов данных
# 2. ЕСЛИ первый запуск:
if not utils.read_players():
    # вывод раздела помощи 
    help.show_help()

# 3. Запрос имени игрока
players.get_name()

# суперцикл (главное меню)
while True:
    # 4. Ожидание ввода команды игрока
    command = input(data.MESSAGES['ввод команды'])
    
    if command in data.COMMANDS['новая партия']:
        game.mode()
        result = game.game()
        if result is not None:
            players.update(result)
    
    # elif command in data.COMMANDS['']:
    
    elif command in data.COMMANDS['выход']:
        break
    
    utils.clear()

# 20. Действия перед завершением работы приложения
