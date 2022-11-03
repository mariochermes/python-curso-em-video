from time import sleep
from random import randint

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
op = int(input('Qual é a sua jogada? '))

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)

comp = randint(1, 3)

print('-=' * 13)
print(f'O computador jogou ', end='')
if comp == 1: print('Pedra')
elif comp == 2: print('Papel')
elif comp == 3: print('Tesoura')
print(f'O jogador jogou ', end='')
if op == 1: print('Pedra')
elif op == 2: print('Papel')
elif op == 3: print('Tesoura')
print('-=' * 13)

if op == comp:
    print('EMPATE')
elif op == 1 and comp == 3 or op == 2 and comp == 1 or op == 3 and comp == 2:
    print('JOGADOR VENCE')
else:
    print('COMPUTADOR VENCE')


