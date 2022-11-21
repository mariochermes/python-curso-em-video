from random import randint

print('Sou seu computador...\nAcabei de pensar um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')

computador = randint(0, 10)
tentativas = jogador = 0

while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador > computador:
        print('Menos... Tente mais uma vez')
    elif computador > jogador:
        print('Mais... Tente mais uma vez')
    else:
        print(f'Acertou com {tentativas} tentativas')
    tentativas += 1

