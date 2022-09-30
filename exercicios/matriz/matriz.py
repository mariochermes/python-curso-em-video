matriz = [[], [], []]
linha = coluna = 0

while linha < 3:
    while coluna < 3:
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(num)
        coluna += 1
    coluna = 0
    linha += 1
print('-=-' * 50)
for l in matriz:
    for n in l:
        print(f'[{n:^5}]', end='')
    print()
