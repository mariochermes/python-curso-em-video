from interface import *


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except:
        print('Erro ao ler o arquivo! ')
    else:
        texto_entrelinhas('PESSOAS CADASTRADAS')
        print(a.read())
        