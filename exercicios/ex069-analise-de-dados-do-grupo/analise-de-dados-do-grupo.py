qtd_adultos = qtd_homens = qtd_mulheres_jovens = 0

while True:
    print('—' * 30)
    print('CADASTRE UMA PESSOA')
    print('—' * 30)

    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().lower()[0]

    if idade > 18:
        qtd_adultos += 1

    if sexo == 'm':
        qtd_homens += 1

    if idade < 20 and sexo == 'f':
        qtd_mulheres_jovens += 1

    continuar = ' '
    while continuar not in 'sn':
        print('—' * 30)
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

print(f'Total de pessoas com mais de 18 anos: {qtd_adultos}')
print(f'Ao todo temos {qtd_homens} homens cadastrado(s)')
print(f'E temos {qtd_mulheres_jovens} mulhere(s) com menos de 20 anos')


    