from time import sleep


def main():
    print('Pesonalize a contagem: ')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    
    print(f'Contagem de {i} até {f} de {p} em {p}')
    contagem(i, f, p)


def contagem(inicio, fim, passo):
    if fim < inicio:
        passo = -passo
    else:
        abs(passo)

    for i in range(inicio, fim, passo):
        sleep(1)
        print(i, end='.. ', flush=True)


main()