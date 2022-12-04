print('-=' * 20)
print('Gerador de PA')
print('-=' * 20)

t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = int(input('Número de iterações: '))
i = t
cont = 0

while(n != 0):
    for i in range(t, t + n * r, r):
        print(f'{i} ->', end=' ')
        cont += 1
    print('PAUSA')
    t = i + r
    n = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {cont} termos mostrados.')