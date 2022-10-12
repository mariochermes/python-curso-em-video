dias = int(input('Quantos dias alugados? '))
deslocamento = float(input('Quantos Km rodados? '))
print(f'O total a pagar é {(dias * 60) + (deslocamento * 0.15):.2f}')