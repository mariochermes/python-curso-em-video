print(f'{" MERCADO ":=^40}')

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

op = int(input('Qual é a sua opção? '))

if op == 1:
    total = 0.9 * preco
    print(f'Sua compra de R${preco:.2f} vai custar R${total} no final')
elif op == 2:
    total = 0.95 * preco
    print(f'Sua compra de R${preco:.2f} vai custar R${total} no final')
elif op == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela}')
elif op == 4:
    parcelas = int(input('Quantas parcelas? '))
    parcela = (preco / parcelas) * 1.2
    total = parcela * parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parcela:.2f} com juros')
    print(f'Sua compra de R${preco:.2f} vai custar R${total} no final')
else:
    print('Opção inválida')
