from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}')
if idade > 18:
    print(f'Você já deveria ter se alistado a {idade - 18} anos')
    print(f'Seu alistamento foi em {date.today().year - (idade - 18)}')
else: 
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {date.today().year + (18 - idade)}')