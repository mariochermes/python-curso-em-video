numeros = []

while True:
    v = int(input('Digite um valor: '))

    if v in numeros:
        print('O valor já está na lista')
    else:
        if len(numeros) == 0:
            index = 0
        else:
            if v < numeros[0]:
                index = 0
            elif v > numeros[len(numeros) - 1]:
                index = len(numeros)
            else:
                for i in range(len(numeros)):
                    if v > numeros[i] and v < numeros[i + 1]:
                        index = i + 1
                        break

        numeros.insert(index, v)
        print(f'Adicionado na posição {index} da lista... ')

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

print('—' * 30)
print(f'Os valores digitados em ordem foram ', end='')
print(*numeros)

