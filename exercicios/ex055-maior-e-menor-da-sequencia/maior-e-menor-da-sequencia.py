pesos = list()

maior = menor = 0

for i in range(0, 5):
    pesos.append(float(input(f'Peso da {i + 1}ª pessoa: ')))
    if i == 0:
        maior = menor = pesos[0]
    if pesos[i] > maior:
        maior = pesos[i]
    if pesos[i] < menor:
        menor = pesos[i]

print(f'O maior peso lido foi de {maior:.1f}')
print(f'O menor peso lido foi de {menor:.1f}')


