matriz = [[], [], []]
soma_pares = soma_terceira_col = 0

for i in range(3):
    for j in range(3):
        while True:
            n = int(input(f'Digite um valor entre 1 e 10 para [{i}, {j}]: '))
            if n in range(1, 10):
                matriz[i].append(n)
                break
            else:
                print('O número deve estar entre 1 e 10')
    
print('—' * 50)
for l in matriz:
    for n in l:
        print(f'[{n:^5}]', end=' ')
    print()
print('—' * 50)

soma_pares = print(sum([sum([n for n in l if n % 2 == 0]) for l in matriz]))
print(f'A soma dos valores pares é {soma_pares}')

for l in range(3):
    soma_terceira_col += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_terceira_col}')

print(f'O maior valor da segunda linha é {max(matriz[1])}')




