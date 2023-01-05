alunos = []

while True:

    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    alunos.append([nome, n1, n2, (n1 + n2) / 2])

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break

print('—' * 50)

print(f"{'No.':<10}{'NOME':<15}{'MÉDIA':<10}")
print('—' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<10}{a[0]:<15}{a[3]:<10.2f}')
print('—' * 30)

while True:
    esc = int(input('Mostrar notas de qual aluno? '))

    print(f'As notas de {alunos[esc][0]} são: {alunos[esc][1]} e {alunos[esc][2]}')

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
    if continuar == 'n':
        break