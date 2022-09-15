def cadastrar():
    arq = open('base_aluno.txt', 'a')
    nome = str(input('Nome: '))
    matricula = int(input('Matrícula: '))
    arq.write(f'Nome: {nome} | Matrícula: {matricula}')


#Main
cadastrar()