print('—' * 30)
print(f"{'LOJA':^30}")
print('—' * 30)

total = qtd_produtos_1000 = menor_valor = 0

while True:

    nome = input('Nome do produto: ')
    valor = float(input('Preço: R$'))

    total += valor

    if valor > 1000:
        qtd_produtos_1000 += 1
    
    if total == valor:
        menor_valor = valor
        produto_mais_barato = nome
    if valor < menor_valor:
        menor_valor = valor
        produto_mais_barato = nome

    continuar = ' '
    while continuar not in 'sn':
        print('—' * 30)
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
        print('—' * 30)
    if continuar == 'n':
        break

print(f"{'FIM DO PROGRAMA':—^30}")

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtd_produtos_1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_mais_barato} que custa R${menor_valor:.2f}')
