alunos = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    média = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], média])
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar ? ')).lower().replace(' ', '')[0]
        if continuar not in 'sn':
            print('Opção inválida')
    if continuar == 'n':
        break
print('—='*20)
print(f'{"Boletim":—^40}')
print('—='*20)
print(f'{"No":<6}{"Nome":<14}{"Notas":<12}{"Média":>8}')
for pos, a in enumerate(alunos):
    print(f'{pos+1:<6}{str(a[0]):<14}{str(a[1]):<12}{str(a[2]):>8}')
while True:
    esc = int(input('Deseja ver a nota de qual aluno ? '))-1
    if esc > len(alunos)-1:
        print('Opção inválida')
    print(f'O aluno {alunos[esc][0]} tirou {alunos[esc][1][0]} e {alunos[esc][1][1]}, sua média foi {alunos[esc][2]}')
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar ? ')).lower().replace(' ', '')[0]
        if continuar not in 'sn':
            print('Opção inválida')
    if continuar == 'n':
        break
print('<<FIM>>')
