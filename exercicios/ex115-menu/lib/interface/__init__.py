from ..validacao import *


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


def linha(tam=42):
    return '—' * tam


def texto_entrelinhas(texto):
    print(linha())
    print(f'{texto}'.center(42))
    print(linha())
    

def menu(lista):
    texto_entrelinhas('MENU PRINCIPAL')

    for i, item in enumerate(lista):
        print(cores(f'{i + 1} -', 'amarelo'), cores(f'{item}', 'azul'))
    print(linha())

    opcao = leia_int('Sua opção: ')

    return opcao

