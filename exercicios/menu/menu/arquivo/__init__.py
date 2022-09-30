import os


def arquivo(nome='Info.txt', ação='r', escrever=''):
    if not os.path.isfile(nome):
        f = open(nome, 'x')
    else:
        if ação == 'r':
            f = open(nome, 'r')
            print(f.read())
        elif ação == 'a':
            f = open(nome, 'a')
            f.write(escrever)
