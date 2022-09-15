from Arquivo import *
from time import sleep


def menu():
    while True:
        cabeçalho('MENU PRINCIPAL')
        print(f'{cores(1, "amarelo")} — {cores("Ver pessoas cadastradas", "azul")}')
        print(f'{cores(2, "amarelo")} — {cores("Cadastrar nova pessoa", "azul")}')
        print(f'{cores(3, "amarelo")} — {cores("Sair do sistema", "azul")}')
        print('—' * 40)
        while True:
            #try:
            op = int(input(f'{cores("Sua opção: ", "amarelo")}'))
            if op == 1:
                ver()
                break
            elif op == 2:
                cadastrar()
                break
            elif op == 3:
                break
            else:
                print(f'{cores("ERRO! Digite uma opção válida!", "vermelho")}')
            """except:
                print(f'{cores("ERRO! por favor digite um número inteiro válido", "vermelho")}')"""
        if op == 3:
            cabeçalho('Até mais...')
            break


def cores(texto, cor='branco'):
    cores = {'limpa': '\033[m',
             'vermelho': '\033[0;31m',
             'verde': '\033[0;32m',
             'amarelo': '\033[0;33m',
             'azul': '\033[0;34m',
             'roxo': '\033[0;35m',
             'branco': '\033[0;97m'
             }
    return f'{cores[f"{cor}"]}{texto}{cores["limpa"]}'


def cabeçalho(texto):
    print('—' * 40)
    print(f'{texto:^40}')
    print('—' * 40)


def ver():
    cabeçalho('Opção 1')
    arquivo()
    sleep(1)


def cadastrar():
    cabeçalho('Opção 2')
    info = dict()
    info['nome'] = str(input('Nome: '))
    info['idade'] = int(input('idade: '))
    pos = 0
    for k, v in info.items():
        arquivo(ação='a', escrever=f'{k}: {v} ')
        if pos < 1:
            arquivo(ação='a', escrever='| ')
        pos += 1
    arquivo(ação='a', escrever='\n')
    sleep(1)


