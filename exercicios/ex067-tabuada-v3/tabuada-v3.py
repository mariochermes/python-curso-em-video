while True:
    n = int(input('Quer ver a tabuada de qual valor (0 para sair)? '))

    if n == 0:
        break

    print('—' * 30)
    for i in range(1, 11):
        print(f'{n:2} x {i:2} = {n * i:2}')
    print('—' * 30)

print('FIM')
