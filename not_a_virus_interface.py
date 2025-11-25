import os

os.system('cls')

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
    print()
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
        print()
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
    settings = off_on_menu(settings, settings_ru)
    cmds()


def heading():
    print(' _______          __               _____           ____   ____.__                     ')
    print(' \      \   _____/  |_            /  _  \          \   \ /   /|__|______ __ __  ______')
    print(' /   |   \ /  _ \   __\  ______  /  /_\  \   ______ \   Y   / |  \_  __ \  |  \/  ___/')
    print('/    |    (  <_> )  |   /_____/ /    |    \ /_____/  \     /  |  ||  | \/  |  /\___ \ ')
    print('\____|__  /\____/|__|           \____|__  /           \___/   |__||__|  |____//____  >')
    print('        \/                              \/                                         \/ ')


def cmds():
    os.system('cls')



    heading()
    print()
    print('1. Начать проверку файла')
    print('2. Проверить на трояны (Недоступно)')
    print('3. Настройки')
    print('4. Открыть интерфес Tkinter (Недоступно)')
    print('5. Админ-Панель (Недоступно)')
    print('6. Сменить язык (Недоступно)')
    print()
    a = input('>>> ')

    if a == '1':
        cmds()
    if a == '3':
        open_settings()

def start():

    heading()

    print()
    print('>>> Yes/No')
    print()
    
    a = input('Вы хотите запустить программу? >>> ')

    if a == 'Yes' or 'yes' or 'y':
        cmds()
    if a == 'No' or 'no' or 'n':
        exit
    else:
        os.system('cls')
        start()

start()
#TODO: лутше зделать с циклом ато так получается ооооооооочень долгий stack, потому что каждая функция дальше просто вызывает другую -> тратит больше памяти
