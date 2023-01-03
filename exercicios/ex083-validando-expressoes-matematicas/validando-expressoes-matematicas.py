print('—' * 30)
print(f"{'VALIDADOR DE PARÊNTESES':^30}")
print('—' * 30)

exp = input('Digite a expressão matemática: ')
tmp = []

for c in exp:
    if c == '(':
        tmp.append(c)
    elif c == ')':
        if len(tmp) > 0:
            tmp.pop()
        else:
            tmp.append(c)
            break

if len(tmp) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
