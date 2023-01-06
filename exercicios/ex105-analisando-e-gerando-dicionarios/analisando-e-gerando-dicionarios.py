def main():
    resp = notas(5.5, 2.5, 1.5, 6)
    print(resp)


def notas(*nota, sit=False):
    dados = {}

    dados['total'] = len(nota)
    dados['maior'] = max(nota)
    dados['menor'] = min(nota)
    dados['média'] = sum(nota) / len(nota)

    return dados


main()
