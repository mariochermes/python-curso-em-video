alunos = []
aluno = []

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno[:])
    aluno.clear()
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar ?')).lower().replace(' ', '')
    if continuar == 'n':
        break
print('—=' * 30)
print(f'{"No.":<6}{"NOME":<10}{"MÉDIA":>10}')
for pos, a in enumerate(alunos):
    print(f'{pos:<6}{a[0]:<10}{(a[1] + a[2])/2:8.1f}')
while True:
    print('—' * 40)
    pos = int(input('Mostrar notas de qual aluno ? '))
    print(f'As notas de {alunos[pos][0]} são: {alunos[pos][1]} e {alunos[pos][2]}')
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar ?')).lower().replace(' ', '')
    if continuar == 'n':
        break