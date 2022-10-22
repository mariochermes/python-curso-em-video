salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:
    print(f'{salario * 1.1:.2f}')
else:
    print(f'{salario * 1.15:.2f}')