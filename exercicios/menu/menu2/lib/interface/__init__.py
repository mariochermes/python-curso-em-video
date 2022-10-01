def leiaInt(msg):
    while True:
        try:
            n = int (input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('Usuário interrompeu o programa')
            return 0
        else:
            return n

def linha(tam=42):
    return '—' * tam

def entreLinhas(txt):
    print(linha(42))
    print(txt.center(42))
    print(linha(42))

def menu(titulo, opçoes):
    entreLinhas(titulo)
    for i, o in enumerate(opçoes):
        print(f'{i + 1} - {o}')
    print('\n')
    opc = leiaInt('Sua opção: ')
    return opc