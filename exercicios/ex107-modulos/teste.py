from moeda import *

p = float(input('Digite o preço: '))
taxa = 10

print(f'A metade de {p} é {metade(p)}')
print(f'A dobro de {p} é {dobro(p)}')
print(f'Aumentando {taxa}%, temos {aumentar(p, taxa)}')