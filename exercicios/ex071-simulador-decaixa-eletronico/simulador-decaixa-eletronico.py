print('—' * 30)
print(f"{'BANCO':^30}")
print('—' * 30)

valor = int(input('Que valor você quer sacar? R$'))

cedulas_50 = valor // 50
valor = valor - cedulas_50 * 50

cedulas_10 = valor // 10
valor = valor - cedulas_10 * 10

cedulas_1 = valor // 1
valor = valor - cedulas_1 * 1

print(f'Total de {cedulas_50} cédulas de R$50')
print(f'Total de {cedulas_10} cédulas de R$10')
print(f'Total de {cedulas_1} cédulas de R$1')

print('—' * 30)


