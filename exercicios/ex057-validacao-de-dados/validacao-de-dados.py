while True:
    sexo = str(input('Informe seu sexo [M/F]: '))

    if sexo not in 'MmFf':
        print('Dados inválidos. Por favor, informe seu sexo: ')
    else:
        print(f'Sexo {sexo.upper} registrado com sucesso')
        break