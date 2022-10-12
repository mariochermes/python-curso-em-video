from time import sleep

nome = input(str('Digite seu nome completo: '))
print('Analisando seu nome...')
sleep(1)
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {nome.replace(" ", "").count()} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {nome.split()[0].count()}')
