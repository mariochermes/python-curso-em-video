def leia_int(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO: \"{n}\" não é um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\033[0;31mERRO: Entrada de dados foi interrompida pelo usuário\033[m")
            return 0
        else:
            return n


def leia_float(texto):
    while True:
        try:
            n = float(input(texto).replace(',', '.'))
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO: \"{n}\" não é um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\033[0;31mERRO: Entrada de dados foi interrompida pelo usuário\033[m")
            return 0
        else:
            return n
            