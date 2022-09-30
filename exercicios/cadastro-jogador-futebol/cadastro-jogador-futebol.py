jogador = {}
jogadores = []
gols = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou ? '))
    gols.clear()
    for p in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {p+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar(s/n) ? ')).lower().replace(' ', '')
        if continuar in 'sn':
            break
        print('Opção inválida, digite apenas "s" ou "n"')
    if continuar == 'n':
        print('—=' * 30)
        break
print(f'{"cod":<6}{"nome":<14}{"gols":<12}{"total":>12}')
print('—' * 50)
for pos, j in enumerate(jogadores):
    print(f'{pos+1:<6}{str(j["nome"]):<14}{str(j["gols"]):<12}{str(j["total"]):>8}')
print('—' * 50)
while True:
    escolha = int(input('Mostrar dados de qual jogador ?'))-1
    if escolha >= len(jogadores):
        print(f'Não existe nenhum jogador o índice {escolha}')
    else:
        print(f'Levantamento do jogador {jogadores[escolha]["nome"]}')
        for pos, g in enumerate(jogadores[escolha]['gols']):
            print(f'Na partida {pos}, {jogadores[escolha]["nome"]} fez {g} gols')
    while True:
        continuar = str(input('Quer continuar(s/n) ? ')).lower().replace(' ', '')
        if continuar in 'sn':
            break
        print('Opção inválida, digite apenas "s" ou "n"')
    if continuar == 'n':
        print('—=' * 30)
        break
print('ENCERRADO')