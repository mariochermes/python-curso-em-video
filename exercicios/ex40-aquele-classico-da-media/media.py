n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, a média do aluno é {media}')

if media >= 7:
    print('O aluno está aprovado')
else:
    print('O aluno está reprovado')
