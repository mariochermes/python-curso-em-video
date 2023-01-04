valores = [[], []]

for i in range(7):
    v = int(input(f'Digite o {i + 1}º valor: '))

    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)

valores[0].sort()
valores[1].sort()

print('—' * 50)
print('Os valores pares digitados foram: ', end='')
print(*valores[0])
print('Os valores ímpares digitados foram: ', end='')
print(*valores[1])