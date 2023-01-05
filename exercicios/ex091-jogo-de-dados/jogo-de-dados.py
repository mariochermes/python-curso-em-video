from random import randint
from time import sleep

jogadores = {}

print('—' * 30)
print(f"{'JOGO DE DADOS':^30}")
print('—' * 30)

qtd_jogadores = int(input('Quantos jogadores vão jogar? '))

for i in range(qtd_jogadores):
    jogadores[f'jogador{i + 1}'] = randint(1, 6)

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')

print('—' * 50)

jogadores = dict(sorted(jogadores.items(),key= lambda x:x[1], reverse=True))

print(f"{' RANKING ':=^30}")
for i, (k, v) in enumerate(jogadores.items()):
    sleep(1)
    print(f"{f'{i + 1}º lugar: {k} com {v}':^30}")
