matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        while True:
            matriz[i].append(int(input(f'Digite um valor entre 1 e 10 para [{i}, {j}]: ')))
            if matriz[i][j] in range(1, 10):
                break
            else:
                print('O número deve estar entre 1 e 10')
    
print('—' * 50)
for l in matriz:
    for n in l:
        print(f'[{n:^5}]', end=' ')
    print()
print('—' * 50)

soma_pares = soma_terceira_col = 0

for l in range(3):
    for c in range(3):
            if matriz[l][c] % 2 == 0:
                soma_pares += matriz[l][c]
            if c == 2:
                soma_terceira_col += matriz[l][c]

print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_col}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')




