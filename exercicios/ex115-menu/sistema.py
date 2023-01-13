from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'pessoas.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])

    if resposta == 1:
        ler_arquivo()
    elif resposta == 2:
        cadastrar_pessoas()
    elif resposta == 3:
        print('Saindo. Até logo')
        break
    else:
        print('ERRO! Digite uma opção válida')

    sleep(1)