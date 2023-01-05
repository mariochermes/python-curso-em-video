alunos = {}

alunos['nome'] = input('Nome: ')
alunos['média'] = float(input('Média: '))

if alunos['média'] >= 7:
    alunos['situação'] = 'aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situacão'] = 'recuperação'
else:
    alunos['situação'] = 'reprovado'

print('—' * 50)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')

    