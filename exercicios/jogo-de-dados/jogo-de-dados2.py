from random import randint
import operator

jogadas = dict()
for j in range(1, 5):
    jogadas[f'jogador {j}'] = randint(1, 6)
jogadas = sorted(jogadas.items(), key=operator.itemgetter(1), reverse=True)
print(jogadas)
for pos, j in enumerate(jogadas):
    print(f'O {j[0]} jogou {j[1]} e ficou em {pos+1}º')

