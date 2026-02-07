import os

def heading():
    os.system('cls')
    os.system('color e')
    print(' _______          __               _____           ____   ____.__                     ')
    print(' \      \   _____/  |_            /  _  \          \   \ /   /|__|______ __ __  ______')
    print(' /   |   \ /  _ \   __\  ______  /  /_\  \   ______ \   Y   / |  \_  __ \  |  \/  ___/')
    print('/    |    (  <_> )  |   /_____/ /    |    \ /_____/  \     /  |  ||  | \/  |  /\___ \ ')
    print('\____|__  /\____/|__|           \____|__  /           \___/   |__||__|  |____//____  >')
    print('        \/                              \/                                         \/ ')

def start():
    heading()
    print()
    print('АДМИН-ПАНЕЛЬ')
    print()
    print('1. Закрыть')
    print('2. История (Временно не работает)')
    print('3. Режим редактора (Временно не работает)')
    print('4. Ручной ввод')
    print()
    print('Временно доступен только ручной ввод.')
    print()
    a = input(' >>> ')

    if a == '1':
        os.startfile('Main.py')
    if a == '2':
        start()
    if a == '3':
        start()
    if a == '4':
        os.startfile('headread.py')
    else:
        start()

start()