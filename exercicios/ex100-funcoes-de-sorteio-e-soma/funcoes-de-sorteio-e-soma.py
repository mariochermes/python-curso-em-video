from time import sleep
from random import randint


def main():
    qtd_valores = int(input('Quantos valores você quer sortear? '))
    valores_sorteados = sorteio(qtd_valores)

    print(f'Sorteando os {qtd_valores} valores da lista: ', end='', flush=True)
    for v in valores_sorteados:
        sleep(1)
        print(v, end=' ', flush=True)
    print(f'\nSomando os valores pares de {valores_sorteados}, temos {soma_pares(valores_sorteados)}')


def sorteio(qtd_valores):
    valores = []
    for i in range(qtd_valores):
        valores.append(randint(1, 10))
    
    return valores


def soma_pares(lista_valores):
    soma = 0
    for v in lista_valores:
        if v % 2 == 0:
            soma += v
    
    return soma


main()