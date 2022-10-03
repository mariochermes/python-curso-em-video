from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'exercicios\menu\menu2\cadastrados.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu("MENU PRINCIPAL", ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        entreLinhas('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif resposta == 2:
        entreLinhas('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        entreLinhas('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida')
    sleep(1)
