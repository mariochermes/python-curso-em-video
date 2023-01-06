def main():
    n = int(input('Digite um número para calcular seu fatorial: '))
    print(f'Calculando {n}! =', end=' ')
        
    print(fatorial(n))


def fatorial(n, show=True):
    fatorial = 1
    for i in range(n, 0, -1):
        if show == True:
            if i == 1:
                print(f'{i} =', end=' ')
            else:
                print(f'{i} x', end=' ')

        fatorial *= i
    return fatorial



main()