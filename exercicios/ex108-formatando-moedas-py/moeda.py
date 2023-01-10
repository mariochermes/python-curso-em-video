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
    