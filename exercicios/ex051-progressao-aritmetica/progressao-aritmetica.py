print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(t1,  t1 + (razao * 9), razao):
    print(f'{i}', end=' → ')
print('FIM')