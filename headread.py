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
    print('РУЧНОЙ ВВОД')
    print()
    print('Ожидание команды..')
    print()
    a = input(' >>> ')
    if a == 'close':
        exit
    if a == '':
        pass

start()