veloc = float(input('Qual é a velocidade atual do carro? '))

if veloc > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de {7 * (veloc - 80):.2f}')

print('Tenha um bom dia! Dirija com segurança!')
