cores = {'limpa': '\033[m',
         'vermelho': '\033[0;30;41m',
         'verde': '\033[0;30;42m',
         'amarelo': '\033[0;30;43m',
         'azul': '\033[0;30;44m',
         'roxo': '\033[0;30;45m',
         'branco': '\033[7;30m'
         }


def ajuda(comando):
    título(f'Acessando o manual do comando "{comando}"', 'azul')
    título(help(comando), 'branco')


def título(msg, cor=''):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('—' * tam)
    print(f'  {msg}')
    print('—' * tam)
    print(cores['limpa'], end='')


# Main
while True:
    título('SISTEMA DE AJUDA pyHELP', 'verde')
    comando = str(input('Função ou Biblioteca: '))
    if comando.lower().replace(' ', '') == 'fim':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 'vermelho')
