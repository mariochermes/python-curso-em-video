from ..interface import *


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
    except:
        print('Erro ao ler o arquivo! ')
    else:
        texto_entrelinhas('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]}{dado[1]:>32} anos')
    finally:
        a.close()


def cadastrar_pessoa(nome_arquivo, nome_pessoa, idade):
    try:
        a = open(nome_arquivo, 'at')
        a.close
    except:
        print('Erro ao ler o arquivo! ')
    else:
        try:
            a.write(f'{nome_pessoa};{idade}\n')
        except:
            print('Houve um erro  na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome_pessoa} adicionado')
        
    
        