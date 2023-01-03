valores  = []

while True:
    valores.append(int(input('Digite um valor: ')))

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

valores.sort(reverse=True)

print('—' * 50)
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente são ', end='')
print(*valores)

if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado')



