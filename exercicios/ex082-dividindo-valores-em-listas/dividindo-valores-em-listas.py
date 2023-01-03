valores = []

while True:
    valores.append(int(input('Digite um valor: ')))

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

pares = [v for v in valores if v % 2 == 0]
impares = [v for v in valores if v % 2 != 0]

print('—' * 50)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
