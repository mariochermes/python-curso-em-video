pessoa = dict()
dados = list()

total_idade = qtd_mulheres = pessoas_acima = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo(m/f): ')).lower().replace(' ', '')[0]
        if pessoa['sexo'] in 'mf':
            break
        print('Por favor digite apenas m ou f')
    if pessoa['sexo'] == 'f':
        qtd_mulheres += 1
    while True:
        pessoa['idade'] = str(input('Idade: ')).lower().strip().replace(' ', '')
        if pessoa['idade'].isnumeric() and 0 < int(pessoa['idade']) < 130:
            pessoa['idade'] = int(pessoa['idade'])
            break
        print('Digite apenas valores válidos para idade')
    total_idade += pessoa['idade']
    dados.append(pessoa.copy())
    continuar = ' '
    while True:
        continuar = str(input('Quer continuar (s/n)? ')).lower().replace(' ', '')[0]
        if continuar in 'sn':
            break
        print('Por favor digite apenas s ou n')
    if continuar == 'n':
        break

print(f'A) {len(dados)} pessoas foram cadastradas.')
print(f'B) A média de idade das pessoas cadastradas é: {total_idade/len(dados):.2f}')
print(f'C) As mulheres cadastradas são: ', end='')
cont = 0
for p in dados:
    if p['sexo'] == 'f':
        print(f'{p["nome"]}', end='')
        cont += 1
        if cont < qtd_mulheres:
            print(', ', end='')
        else:
            print('.')
print('D) As pessoas cadastradas com idade acima da média são: ', end='')
for p in dados:
    if p['idade'] > total_idade/len(dados):
        pessoas_acima += 1
cont = 0
for p in dados:
    if p['idade'] > total_idade / len(dados):
        print(f'{p["nome"]}', end='')
        cont += 1
        if cont < pessoas_acima:
            print(', ', end='')
        else:
            print('.')
print('<<FIM>>')