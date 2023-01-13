from ..validacao import *

cores = {'limpa': '\033[m',
            'vermelho': '\033[0;31m',
            'verde': '\033[0;32m',
            'amarelo': '\033[0;33m',
            'azul': '\033[0;34m',
            'roxo': '\033[0;35m',
            'branco': '\033[0;97m'
            }


def linha (tam=42):
    return '—' * tam


def texto_entrelinhas(texto, cor=cores['branco']):
    print(cor, end='')
    print(linha())
    print(f'{texto}'.center(42))
    print(linha())
    print(cores['limpa'], end='')


def menu(lista):
    texto_entrelinhas('MENU PRINCIPAL')

    for i, item in enumerate(lista):
        print(f'{i + 1} - {item}')
    print(linha())

    opcao = leia_int('Sua opção: ')

    return opcao

