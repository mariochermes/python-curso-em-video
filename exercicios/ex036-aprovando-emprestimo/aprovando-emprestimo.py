valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = valor / (tempo * 12)

print(f'Para pegar uma casa de R${valor:.2f} em {tempo} anos a prestação será de {prestacao:.2f}')

if prestacao > 0.3 * salario:
    print('empréstimo NEGADO')
else:
    print('empréstimo APROVADO')