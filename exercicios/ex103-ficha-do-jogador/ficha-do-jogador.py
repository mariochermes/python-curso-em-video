def main():
    n = str(input('Nome do jogador: '))
    g = str(input('Número de gols: '))

    ficha(n, g)


def ficha(nome='<desconhecido>', gols=0):
    if not nome.isalpha():
        nome='<desconhecido>'

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


main()