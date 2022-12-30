print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)

termos = int(input('Quantos termos você quer mostrar? '))

t1 = 0 
t2 = 1
print(f'{t1} -> {t2}', end=' ')

for i in range(3, termos):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'-> {t3}', end=' ')
print('-> FIM')
