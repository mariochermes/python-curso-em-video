from time import sleep

v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))

while True:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    op = int(input('Qual é a sua opção: '))

    if op == 1:
        print(f'A soma entre {v1} e {v2} é {v1 + v2}')
    elif op == 2:
        print(f'A multiplicação entre {v1} e {v2} é {v1 * v2} ')
    elif op == 3:
        if v1 > v2:
            print(f'{v1} é maior que {v2}')
        elif v1 < v2:
            print(f'{v2} é maior que {v1}')
        else:
            print('Os números são iguáis')
    elif op == 4:
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))
    elif op == 5:
        break
    else:
        print('Opção inválida')
    print('–' * 40)
    sleep(1)
print('Até logo!')
