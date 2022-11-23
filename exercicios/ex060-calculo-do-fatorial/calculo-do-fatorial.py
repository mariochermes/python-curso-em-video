def fatorial(num):
    if num == 1:
        return num
    
    return num * fatorial(num - 1)

n = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {n}! =', end=' ')
for i in range(n, 0, -1):
    if i == 1:
        print(f'{i} =', end=' ')
    else:
        print(f'{i} x', end=' ')
        
print(fatorial(n))