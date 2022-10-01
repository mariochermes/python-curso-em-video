from time import sleep
from lib.interface import *


while True:
    resposta = menu("MENU PRINCIPAL", ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        entreLinhas('Opção 1')
    elif resposta == 2:
        entreLinhas('Opção 2')
    elif resposta == 3:
        entreLinhas('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida')
    sleep(1)
