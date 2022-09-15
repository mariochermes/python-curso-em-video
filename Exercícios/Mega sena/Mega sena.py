from time import sleep
from random import randint

jogo = []
jogos = []

print('''
———————————————————————————————
       JOGA NA MEGA SENA
———————————————————————————————
''')

num_jogos = int(input('Quantos jogos você quer que eu sorteie ? '))

print('-=-=-= SORTEANDO 5 JOGOS -=-=-=')
for j in range(0, num_jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    sleep(1)
    print(f'Jogo {j+1}: {jogo}')
    jogos.append(jogo[:])
    jogo.clear()
print('-=-=-=-= < BOA SORTE > -=-=-=-=')
print(jogos)
