preço = total = produto_maior_1000 = cont = menor_preço = 0
produto_mais_barato = produto = ' '

while True:
    print('''
    |~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    |        NERD STORE         |
    |~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    ''')

    produto = str(input('Nome do produto: ')).lower().replace(' ', '')
    preço = float(input('Preço do Produto: '))

    total += preço

    if preço > 1000:
        produto_maior_1000 += 1
    if cont == 0:
        produto_mais_barato = produto
        menor_preço = preço
    if preço < menor_preço:
        produto_mais_barato = produto
        menor_preço = preço
    cont += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Você deseja continuar ? (s/n)').lower().replace(' ', '')[0]
    if continuar == 'n':
        break
print(f'\nO total gasto na compra foi {total}')
print(f'{produto_maior_1000} custam mais que R$1000')
print(f'O produto mais barato foi: {produto_mais_barato} ')
