from datetime import date

nascimentos = list()

maiores = 0
menores = 0

for i in range(0, 7):
    nascimentos.append(int(input(f'Em que ano a {i + 1}ª pessoa nasceu: ')))
    if date.today().year - nascimentos[i] >= 18:
        maiores += 1
    else:
        menores += 1

print(f'\nAo todo tivemos {maiores} pessoas maiores de idade')
print(f'Ao todo tivemos {menores} pessoas menores de idade')