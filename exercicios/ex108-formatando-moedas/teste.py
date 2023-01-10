from moeda import *

p = float(input('Digite o preço: '))
taxa = 10

print(f'A metade de {moeda(p)} é {metade(p, form=True)}')
print(f'A dobro de {moeda(p)} é {dobro(p, form=True)}')
print(f'Aumentando {taxa}%, temos {aumentar(p, taxa, form=True)}')