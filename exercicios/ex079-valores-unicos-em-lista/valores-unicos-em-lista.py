numeros = []

while True:
    n = int(input('Digite um valor: '))

    if n in numeros:
        print('Valor já está na lista, não será adicionado novamente')
    else:
        numeros.append(n)
        print('Valor adicionado com sucesso!')

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

print('—' * 30)
print(f'Você digitou os valores ', end='')
print(*numeros)


