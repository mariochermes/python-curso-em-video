from time import sleep
from random import randint

jogo = []

print('—' * 30)
print(f"{'MEGA SENA':^30}")
print('—' * 30)

qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 3 + f' SORTEANDO {qtd_jogos} JOGOS ' + '-=' * 3)
for i in range(qtd_jogos):
    print(f'Jogo {i + 1}: ', end='')
    for j in range(6):
        v = randint(1, 100)
        jogo.append(v)
        print(v, end=' ')
    print()
print('-=' * 15)
    