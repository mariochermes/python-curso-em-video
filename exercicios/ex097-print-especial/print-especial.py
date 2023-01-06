def main():
    texto_entrelinhas(str(input('Texto: ')))


def texto_entrelinhas(texto):
    print('—' * (len(texto) + 4))
    print(f'  {texto}')
    print('—' * (len(texto) + 4))


main()