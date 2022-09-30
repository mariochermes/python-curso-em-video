import random

jogador = computador = vitórias = 0

while True:
    escolha = ' '
    print('~' * 50)
    while escolha not in 'pi':
        escolha = str(input('Você quer par ou ímpar ? [P/I] ')).strip().lower().replace(' ', '')[0]
        if escolha not in 'pi':
            print('Opção inválida')
    jogador = int(input('Digite um valor entre 0 e 10: '))
    if 0 <= jogador <= 10:
        computador = random.randint(0, 10)
        if escolha == 'p':
            if (jogador + computador) % 2 != 0:
                print('Você jogou {} e o computador {}. Total de {} deu IMPAR'.format(jogador, computador, jogador + computador))
                print('Você perdeu !')
                break
            elif (jogador + computador) % 2 == 0:
                print('Você jogou {} e o computador {}. Total de {} deu PAR'.format(jogador, computador, jogador + computador))
                print('Você venceu ! Jogue novamente')
                vitórias += 1
        elif escolha == 'i':
            if (jogador + computador) % 2 != 0:
                print('Você jogou {} e o computador {}. Total de {} deu IMPAR'.format(jogador, computador, jogador + computador))
                print('Você venceu ! Jogue novamente')
                vitórias += 1
            elif (jogador + computador) % 2 == 0:
                print('Você jogou {} e o computador {}. Total de {} deu PAR'.format(jogador, computador, jogador + computador))
                print('Você perdeu !')
                break
    else:
        print('Opção inválida')
print('Fim de jogo, você ganhou {} veze(s)'.format(vitórias))
print('~' * 50)

