import os
os.system('cls')
os.system('color e')


def heading():
    print(' _______          __               _____           ____   ____.__                     ')
    print(' \\      \\   _____/  |_            /  _  \\          \\   \\ /   /|__|______ __ __  ______')
    print(' /   |   \\ /  _ \\   __\\  ______  /  /_\\  \\   ______ \\   Y   / |  \\_  __ \\  |  \\/  ___/')
    print('/    |    (  <_> )  |   /_____/ /    |    \\ /_____/  \\     /  |  ||  | \\/  |  /\\___ \\ ')
    print('\\____|__  /\\____/|__|           \\____|__  /           \\___/   |__||__|  |____//____  >')
    print('        \\/                              \\/                                         \\/ ')
    print()
    print('0. Выйти')
    print('1. Открыть CMD Интерфейс')
    print('2. Открыть Tkinter Интерфейс (BETA)')
    print()
    print('ПРОГРАММА НАХОДИТСЯ В BETA ТЕСТЕ И СОДЕРЖИТ БАГИ')
    print()
    a = input('>>> ')

    if a == '1':
        cm.start()
        # os.startfile('cm.py')
    if a == '2':
        tk.main()
        # os.startfile('tk.py')

heading()
