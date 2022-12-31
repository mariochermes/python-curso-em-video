from random import randint

print('—' * 30)
print(f"{'PAR OU IMPAR':^30}")
print('—' * 30)

vitorias = 0
while True:

    escolha = input('Par ou Ímpar (P/I)? ').strip().lower()[0]
    if escolha not in 'pi':
        continue

    jog = int(input('Digite um valor de 1 a 10: '))
    if jog > 10:
        continue

    comp = randint(1, 10)
    total = jog + comp

    print('—' * 30)
    print(f'Você jogou {jog} e o computador {comp}. O total de {total} é ', end='')
    print('PAR'if (total) % 2 == 0 else 'ÍMPAR')
    print('—' * 30)

    if escolha == 'p':
        if (total) % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    else:
        if (total) % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você venceu!')
            vitorias += 1

print('—' * 30)
print(f'GAME OVER! Você venceu {vitorias} vezes')



