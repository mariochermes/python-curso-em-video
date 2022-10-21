from random import randint
from time import sleep

print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 30)

n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)

ale = randint(0, 5)

if ale == n:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {ale} e não no {n}!')
