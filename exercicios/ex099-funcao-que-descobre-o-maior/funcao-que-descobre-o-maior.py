from time import sleep


def main():
    numeros = []

    qtd_numeros = int(input('Quantos números você quer passar? '))

    for i in range(qtd_numeros):
        numeros.append(input(f'Digite o {i + 1}º número: '))
    
    print('Analisando os valores passados...')
    sleep(1)
    print(f'Foram informados {len(numeros)} valores ao todo')
    print(*numeros)
    print(f'O maior valor informado foi {maior(numeros)}')


def maior(lista_numeros):
    return max(lista_numeros)


main()