from math import sqrt

cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {sqrt(cat_oposto ** 2 + cat_adjacente ** 2):.2f}')