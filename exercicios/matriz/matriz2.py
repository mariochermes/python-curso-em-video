matriz = [[], [], [], []]

for linha, l in enumerate(matriz):
    for n in range(0, 4):
        l.append(0)
    for coluna, c in enumerate(l):
        if coluna > linha:
            matriz[linha][coluna] = (2 * linha) + (2 * coluna)
        elif linha > coluna:
            matriz[linha][coluna] = (3 * linha) + (3 * coluna)
        elif linha == coluna:
            matriz[linha][coluna] = (4 * linha) + (4 * coluna)
print(matriz)

for linha, l in enumerate(matriz):
    print('{', end='')
    for coluna, c in enumerate(l):
        print(f'{c:^5}', end='')
        if coluna+1 < len(l):
            print(',', end='')
    print('}')
