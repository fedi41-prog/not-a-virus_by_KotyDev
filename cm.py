import os
from tkinter import filedialog
from colorama import Fore, Back, Style
import time

launge = 2

os.system('cls')
os.system('color e')

settings = {
    "option 1":False,
    "option 2":False,
    "option 3":False
}
settings_ru = {
    "option 1":"Первая настройка",
    "option 2":"Вторая настройка",
    "option 3":"Третья настройка"
}

# так просто может полезная функция (:
def choose(options):
    n = len(options)

    print("0. Назад")
    for i in range(1, n + 1):
        state = "ON" if options[i] else "OFF"
        print(f"{i}. {options[i]} ({state})")

    inp = input(">>> ").strip()
    if inp == "0": return
    if inp.isdigit():
        int_inp = int(inp)
        if 0 < int_inp < n:
            return options[int_inp]

# off-on menu!
def off_on_menu(settings_states:dict[str, bool], settings_text:dict[str:str]=None):
    """
    меню для (off-on) настроек. Меняет переданные настройки
    :param settings_states: все параметры и их позиция (off-on)
    :param settings_text: текст параметров
    :return: те же настройки
    """
    map_id_to_setting = {}
    i = 1
    for s in settings_states.keys():
        map_id_to_setting[i] = s
        i += 1

    while True:
        os.system('cls')
        heading()

        n = len(settings_states)

        print("0. Назад")
        i = 1
        for s, st in settings_states.items():
            print(f"{i}. {settings_text[s]} ({'ON' if st else 'OFF'})")
            i += 1

        inp = input(">>> ").strip()
        if inp == "0": return settings_states
        if inp.isdigit():
            int_inp = int(inp)
            if 0 < int_inp <= n:
                settings_states[map_id_to_setting[int_inp]] = not settings_states[map_id_to_setting[int_inp]]





def open_settings():
    global settings
    print('Временно не работает')
    print()
    settings = off_on_menu(settings, settings_ru)
    if launge == 2:
        cmds()
    if launge == 1:
        engcmds()

def heading():
    print(' _______          __               _____           ____   ____.__                     ')
    print(' \      \   _____/  |_            /  _  \          \   \ /   /|__|______ __ __  ______')
    print(' /   |   \ /  _ \   __\  ______  /  /_\  \   ______ \   Y   / |  \_  __ \  |  \/  ___/')
    print('/    |    (  <_> )  |   /_____/ /    |    \ /_____/  \     /  |  ||  | \/  |  /\___ \ ')
    print('\____|__  /\____/|__|           \____|__  /           \___/   |__||__|  |____//____  >')
    print('        \/                              \/                                         \/ ')


def check_one():
    os.system('cls')
    os.system('color 0')
    alert_words = [['shutdown', ''], ['echo', '>'],
    [':', 'goto'], ['del', '/s', '/q', 'C:\\', '*.*'],
    ['rmdir', '/s', '/q', 'C:\\'], ['net', 'user'],
    ['net', 'localgroup', '/add'],]

    def print_list(list_):
        return ', '.join(list_)


    def check_file(filename, encoding='utf-8'):
        if os.path.exists(filename):
            with open(filename, 'r', encoding=encoding) as f:
                contents = f.read()
                contents_list = contents.split('\n')
                for line in contents_list:
                    for words in alert_words:
                        x = True
                        true_words = []
                        c = 0
                        for word in words:
                            true_words.append(word)
                            c += 1
                            if word not in line:
                                x = False
                                break
                        if x:
                            print(f'{Fore.LIGHTYELLOW_EX}Найдено: {Fore.LIGHTRED_EX}{print_list(true_words)}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}')
                            print()
                                    
        else:
            print("File not found")

    file = filedialog.askopenfile(title="Select file",

    filetypes=(("bat", "*.bat"), ("all files", "*.*")))

    check_file(file.name)

    a = input('Press Enter >>> ')
    os.system('cls')
    os.system('color e')
    if launge == 2:
        cmds()
    if launge == 1:
        engcmds()

def cmds():
    os.system('cls')
    os.system('color e')



    heading()
    print()
    print('1. Начать проверку файла')
    print('2. Проверить на трояны (В разработке)')
    print('3. Настройки (Работает Частично)')
    print('4. Открыть интерфес Tkinter')
    print('5. Админ-Панель (В разработке)')
    print('6. Сменить язык (В разработке)')
    print()
    a = input('>>> ')

    if a == '1':
        check_one()
        print(a)
    if a == '3':
        open_settings()
    if a == '4':
        os.startfile('tk.py')
    if a == '6':
        os.system('cls')
        heading()
        print()
        print('0. Назад')
        print('1. English')
        print('2. Русский')
        print()
        a = input('>>> ')
        if a == 0:
            os.system('cls')
            cmds()
        if a == 1:
            os.system('cls')
            engcmds()
            launge = 1
        if a == 2:
            os.system('cls')
            launge = 2
            cmds()
    else:
        if launge == 2:
            cmds()
        if launge == 1:
            engcmds()
        cmds()

def engcmds():
    os.system('cls')
    os.system('color e')



    heading()
    print()
    print('1. Start file scan')
    print('2. Check for Trojans (In development)')
    print('3. Settings (Partially working)')
    print('4. Open Tkinter interface')
    print('5. Admin Panel (In development)')
    print('6. Change language (In development)')
    print()
    a = input('>>> ')

    if a == '1':
        check_one()
        print(a)
    if a == '3':
        open_settings()
    if a == '4':
        os.startfile('tk.py')
    if a == '6':
        os.system('cls')
        heading()
        print()
        print('0. Назад')
        print('1. English')
        print('2. Русский')
        print()
        a = input('>>> ')
        if a == 0:
            os.system('cls')
            cmds()
        if a == 1:
            os.system('cls')
            launge = 1
            engcmds()
        if a == 2:
            os.system('cls')
            launge = 2
            cmds()

def start():
    os.system('color e')
    heading()
    print()
    print('Запуск..')
    time.sleep(1)
    os.system('cls')
    cmds()

start()
