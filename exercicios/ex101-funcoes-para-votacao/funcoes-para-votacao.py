from datetime import date


def main():
    nasc = int(input('Em que ano você nasceu? '))
    print(voto(nasc))


def voto(nascimento):
    idade = date.today().year - nascimento
    
    if idade < 16:
        return f'Com {idade}: VOTO NEGADO'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade}: VOTO OPCIONAL'
    else:
        return f'Com {idade}: VOTO OBRIGATÓRIO'


main()