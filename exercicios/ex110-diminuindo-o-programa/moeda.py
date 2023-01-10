def aumentar(preco, taxa, form=False):
    if form == True:
        return moeda(preco + (taxa / 100) * preco)
    else:
        return preco + (taxa / 100) * preco


def diminuir(preco, taxa, form=False):
    if form == True:
        return moeda(preco - (taxa / 100) * preco)
    else:
        return preco - (taxa / 100) * preco


def dobro(preco, form=False):
    if form == True:
        return moeda(preco * 2)
    else:
        return preco * 2 


def metade(preco, form=False):
    if form == True:
        return moeda(preco / 2)
    else:
        return preco / 2


def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxad=5):
    print('—' * 32)
    print('RESUMO DO VALOR'.center(32))
    print('—' * 32)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxaa}% de redução: \t{diminuir(preco, taxad, True)}')
    print('—' * 32)
    