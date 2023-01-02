tam = int(input('Insira o tamanho da lista: '))
lista = []

for i in range(0, tam):
    lista.append(int(input(f'Digite um valor para a posição {i + 1}: ')))

print('—' * 40)

print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, n in enumerate(lista):
    if n == max(lista):
        print(f'{i + 1}... ', end='')
print()

print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')
for i, n in enumerate(lista):
    if n == min(lista):
        print(f'{i + 1}... ', end='')

