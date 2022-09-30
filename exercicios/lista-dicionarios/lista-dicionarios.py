pessoa = dict()
pessoas = list()
total_idade = 0

cont = 1
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'mf':
        pessoa['sexo'] = str(input('Sexo(m/f): ')).lower().replace(' ', '')
        if pessoa['sexo'] not in 'mf':
            print('ERRO! Por favor, digite apenas m ou f')
    pessoa['idade'] = int(input('Idade: '))
    total_idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar (s/n)?')).lower().replace(' ', '')
        if continuar not in 'sn:':
            print('ERRO! Responda apenas com s ou n')
    print('—' * 30)
    if continuar == 'n':
        break
    cont += 1
print(f'A) Ao todo temos {cont} pessoas cadastradas')
print(f'B) A média de idade é de {total_idade/cont}')
print(f'C) As mulheres cadastradas foram: ', end='')
for pos, p in enumerate(pessoas):
    for k, v in p.items():
        if k == 'sexo':
            if v == 'f':
                print(f'{pessoas[pos]["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média de idade: ')
for pos, p in enumerate(pessoas):
    for k, v in p.items():
        if k == 'idade':
            if v > total_idade/cont:
                print('     ', end='')
                for k2, v2 in p.items():
                    print(f' {k2} = {v2};', end='')
                print()
print('<< ENCERRADO >>')

