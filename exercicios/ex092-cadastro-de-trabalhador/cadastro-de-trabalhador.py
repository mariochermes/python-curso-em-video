from datetime import date

pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35) - date.today().year

print('—' * 50)

for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')