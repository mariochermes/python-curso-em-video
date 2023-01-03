pessoas = []

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))

    if len(pessoas) == 0:
        maior_peso = menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

    pessoas.append([nome, peso])

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

print('—' * 40)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior_peso}. Peso de ', end='')
print(*[p[0] for p in pessoas if p[1] == maior_peso])
print(f'O maior peso foi de {menor_peso}. Peso de ', end='')
print(*[p[0] for p in pessoas if p[1] == menor_peso])
