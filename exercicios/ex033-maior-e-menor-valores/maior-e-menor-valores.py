n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

numeros = [n1, n2, n3]
numeros.sort(reverse = True)

print(f'O maior número é {numeros[0]}')
print(f'O menor número é {numeros[2]}')
