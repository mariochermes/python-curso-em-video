soma = 0
cont = 0
for i in range(0, 501, 3):
    if (i % 2 != 0):
        print(i, end=' ')
        soma += i
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')