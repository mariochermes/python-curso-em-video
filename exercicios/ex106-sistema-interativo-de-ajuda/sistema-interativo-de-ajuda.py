cores = {'limpa': '\033[m',
            'vermelho': '\033[0;31m',
            'verde': '\033[0;32m',
            'amarelo': '\033[0;33m',
            'azul': '\033[0;34m',
            'roxo': '\033[0;35m',
            'branco': '\033[0;97m'
            }


def main():
    texto_entrelinhas('SISTEMA DE AJUDA', cores['verde'])

    comando = ''
    while True:
        comando = input('Função ou Biblioteca > ').lower()
        if comando == 'fim':
            break
        else:
            ajuda(comando)
    
    texto_entrelinhas('ENCERRADO', cores['vermelho'])


def ajuda(com):
    texto_entrelinhas(f'Acessando o manual do \'{com}\'', cores['azul'])
    help(com)


def texto_entrelinhas(texto, cor=cores['branco']):
    print(cor, end='')
    print('—' * (len(texto) + 4))
    print(f'  {texto}')
    print('—' * (len(texto) + 4))
    print(cores['limpa'], end='')


main()