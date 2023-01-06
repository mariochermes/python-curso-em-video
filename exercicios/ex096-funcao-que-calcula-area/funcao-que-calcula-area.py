def main():
    print('Controle de Terrenos')
    print('—' * 20)

    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))

    print(f'A área de um terro {l}x{c} é de {calcular_area(l, c):.2f}')


def calcular_area(largura, comprimento):
    return largura * comprimento


main()
