from moeda import *

p = float(input('Digite o preço: '))
taxa = 10

print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'A dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando {taxa}%, temos {moeda(aumentar(p, taxa))}')