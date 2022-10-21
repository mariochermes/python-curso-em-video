dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dist:.2f}Km')

if dist <= 200:
    print(f'E o preço da sua passagem será de R${dist * 0.5:.2f}')
elif dist > 200:
    print(f'E o preço da sua passagem será de R${dist * 0.45:.2f}')