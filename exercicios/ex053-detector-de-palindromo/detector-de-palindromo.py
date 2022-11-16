frase = str(input('Digite uma frase: ')).lower()

frase_inversa = ''
for i, l in enumerate(frase):
    frase_inversa += frase[len(frase) - 1 - i]


print(f'O inverso de {frase} é {frase_inversa}')

if (frase.replace(' ', '') == frase_inversa.replace(' ', '')):
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')