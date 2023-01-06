jogadores = []
jogador = {}
gols = []

while True: 
    jogador['nome'] = input('Nome: ')

    qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for i in range (qtd_partidas):
        gols.append(int(input(f'    Quantos gols na partida {i + 1}: ')))
        
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    gols.clear()
    jogador.clear()

    while True:
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
        if continuar in 'sn':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if continuar == 'n':
        break

print('-=' * 50)
print(f"{'cod':<15}{'nome':<15}{'gols':<15}{'total':>5}")
print('—' * 50)
for i, j in enumerate(jogadores):
    print(f"{i + 1:<15}{j['nome']:<15}{str(j['gols']):<15}{j['total']:>5}")
print('—' * 50)

while True:
    esc = int(input('Mostrar dados de qual jogador? ')) - 1
    
    print(f"O jogador {jogadores[esc]['nome']} jogou {len(jogadores[esc]['gols'])} partidas")
    for i in range(len(jogadores[esc]['gols'])):
        print(f"    Na partida {i + 1}, fez {jogadores[esc]['gols'][i]} gols")
    print(f"Foi um total de {jogadores[esc]['total']} gols")

    while True:
        continuar = input('Quer continuar (S/N)? ').strip().lower()[0]
        if continuar in 'sn':
                break
        print('ERRO! Por favor, digite apenas S ou N')
    if continuar == 'n':
        break

print('ENCERRADO')
