lista = list()
maior = 0

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        lista.append(num)
        print('{} foi adicionado ao final da lista...'.format(num))
    else:
        for n in lista:
            if num > n:
                maior += 1
        lista.insert(maior, num)
        print('{} foi adicionado a posição {}'.format(num, maior))
        maior = 0
print(lista)

