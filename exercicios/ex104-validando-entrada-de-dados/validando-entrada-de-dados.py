def main():
    n = leia_int('Digite um número: ')
    print(f'Você acabou de digitar o número {n}')


def leia_int(texto):
    while True:
        num_int = str(input(texto))
        if not num_int.isnumeric():
            print('ERRO! Digite um número inteiro válido')
        else:
            return int(num_int)


main()
