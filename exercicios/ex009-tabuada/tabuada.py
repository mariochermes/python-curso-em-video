n = int(input('Digite um número para ver sua tabuada: '))

print('—' * 16)
for i in range(1, 11):
    print(f'{n:<2}{"x":^5}{i:>2}{"=":^5}{n * i:>2}')
print('—' * 16)