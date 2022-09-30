pessoas = list()
pesados = list()
leves = list()
pesado = leve = 0

while True:
    dados = list()
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar (s/n) ?').lower().replace(' ', ''))
    if continuar == 'n':
        break
for pos, p in enumerate(pessoas):
    if pos == 0:
        pesado = leve = p[1]
    else:
        if p[1] > pesado:
            print(f'{p[1]} > {pesado}')
            pesado = p[1]
        if p[1] < leve:
            print(f'{p[1]} < {leve}')
            leve = p[1]
for p in pessoas:
    if pesado == p[1]:
        pesados.append(p[0])
    if leve == p[1]:
        leves.append(p[0])
print('-=-' * 50)
print('Você cadastrou {} pessoas'.format(len(pessoas)), end='')
print('O maior peso foi de {}. Peso de '.format(pesado))
for p in pesados:
    print(f'{p} ', end='')
print('\nO menor peso foi de {}. Peso de '.format(leve), end='')
for p in leves:
    print(f'{p} ', end='')

