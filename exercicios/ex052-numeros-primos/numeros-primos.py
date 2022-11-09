num = int(input('Digite um número: '))
cont_div = 0

for i in range(1, num + 1):
    if num % i == 0:
        cont_div += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{i}\033[m', end=' ')

print(f'\nO número {num} foi divisível {cont_div} vezes')
if cont_div > 2:
    print('E por isso ele não é primo')
else:
    print('E por isso ele é primo')