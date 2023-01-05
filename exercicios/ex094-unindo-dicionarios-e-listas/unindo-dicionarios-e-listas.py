pessoas = []
dados = {}

while True:
    dados['nome'] = input('Nome: ')
    dados['idade'] = int(input('Idade: '))
    while True:
        dados['sexo'] = input('Sexo (M/F): ').strip().lower()[0]
        if dados['sexo'] not in 'mf':
            print('ERRO! Por favor, digite apenas M ou F')
        else:
            break

    pessoas.append(dados.copy())
    dados.clear()

    while True:
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
        if continuar not in 'sn':
            print('ERRO! Por favor, digite apenas S ou N')
        else:
            break
    if continuar == 'n':
        break

media_idade = sum([p['idade'] for p in pessoas]) / len(pessoas)
mulheres_cadastradas = [p['nome'] for p in pessoas if p['sexo'] == 'f']

print('—' * 50)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'A média de idade é de {media_idade:.2f}')
print(f'As mulheres cadastradas foram ')
print(*mulheres_cadastradas)
print('Lista de pessoas que estão acima da média: ')
for p in pessoas:
    for k, v in p.items():
        print(f' {k} = {v}; ', end='')
    print()
print(' —— ENCERRADO ——')