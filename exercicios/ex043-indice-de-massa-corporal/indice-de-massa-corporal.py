peso = float(input('Digite o peso (Kg)? '))
alt = float(input('Digite a altura (m)? '))

imc = peso / (alt**2)
print(f'O IMC dessa pessoa é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')