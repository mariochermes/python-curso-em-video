print('Gerador de PA')
print('-=' * 20)

t1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = int(input('Número de iterações: '))

for i in range(t1, t1 + n * r, r):
    print(f'{i} ->', end=' ')
print('FIM')