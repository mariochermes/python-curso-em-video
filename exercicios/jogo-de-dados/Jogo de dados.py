from random import randint
from time import sleep
from operator import itemgetter

jogada = dict()

for j in range(1, 5):
    rand = randint(1, 6)
    jogada[f'jogador {j}'] = rand
for k, v in jogada.items():
    print(f'O {k} jogou {v}')
    ##sleep(1)
for i in sorted(jogada, key=jogada.get, reverse=True):
    print(f'{i} jogou {jogada[i]}')



