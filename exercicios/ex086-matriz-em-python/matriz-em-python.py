matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('—' * 50)

for l in matriz:
    for n in l:
        print(f'[{n:^5}]', end=' ')
    print()
