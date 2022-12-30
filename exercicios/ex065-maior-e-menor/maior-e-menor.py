cont = media = soma = maior = menor = 0

while True:
    n = int(input('Digite um número: '))

    cont += 1
    soma += n

    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

    continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')