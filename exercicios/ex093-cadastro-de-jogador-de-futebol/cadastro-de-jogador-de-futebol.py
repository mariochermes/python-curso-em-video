jogador = {}
gols = []

jogador['nome'] = input('Nome: ')

qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for i in range (qtd_partidas):
    gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
    
jogador['gols'] = gols
jogador['total'] = sum(gols)

print('—' * 60)
print(jogador)
print('—' * 60)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('—' * 60)

print(f"O jogador {jogador['nome']} jogou {len(gols)} partidas")
for i in range(len(gols)):
    print(f" - Na partida {i + 1}, fez {jogador['gols'][i]} gols")
print(f"Foi um total de {jogador['total']} gols")


        