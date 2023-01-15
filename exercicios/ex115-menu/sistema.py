from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'pessoas.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        texto_entrelinhas('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar_pessoa(arq, nome, idade)
    elif resposta == 3 or resposta == 0:
        print('Saindo. Até logo')
        break
    else:
        print(cores('ERRO! Digite uma opção válida', 'vermelho'))

    sleep(1)