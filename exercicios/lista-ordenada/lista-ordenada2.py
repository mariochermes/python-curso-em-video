lista = list()

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('{} foi adicionado ao final da lista...'.format(num))
    else:
        for pos, n in enumerate(lista):
            if num <= n:
                lista.insert(pos, num)
                print('{} foi adicionado a posição {}'.format(num, pos))
                break
print(lista)

