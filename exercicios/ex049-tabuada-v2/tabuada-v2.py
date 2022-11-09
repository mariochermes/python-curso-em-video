n = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11, 1):
    print(f'{n:<3} x {i:>3}  = {n * i:>3}')