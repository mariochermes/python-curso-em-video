from os import name
from time import sleep

n = int(input('Informe um número na casa dos milhares: '))
print(f'Analisando o número {n}...')
sleep(1)
print(f'Unidade: {str(n)[3]}')
print(f'Dezena: {str(n)[2]}')
print(f'Centena: {str(n)[1]}')
print(f'Milhar: {str(n)[0]}')