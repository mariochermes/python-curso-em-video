soma = 0

for i in range(0, 6):
    n = int(input(f'Digite o {i + 1}º número inteiro: '))
    if n % 2 == 0:
        soma += n

print(f'A soma dos números pares digitados é {soma}')