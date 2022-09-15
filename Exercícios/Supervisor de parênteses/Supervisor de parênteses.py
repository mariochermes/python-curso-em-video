lista = []

exp = str(input('Digite uma expressão: '))

for c in exp:
    if c == '(':
        lista.append(c)
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
print(lista)
if lista == list():
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
print














