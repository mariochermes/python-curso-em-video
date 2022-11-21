nomes = []
idades = []
sexos = []

soma_idades = mais_velho = mulheres_jovens = 0

for i in range (0, 4):
    print('–' * 5, f' {i + 1}ª PESSOA', '–' * 5)
    nomes.append(str(input('Nome: ')))
    idades.append(int(input('Idade: ')))
    sexos.append( str(input('Sexo [M/F]: ')))
    
    soma_idades += idades[i]

    if sexos[i] == 'M' and idades[i] > mais_velho:
        mais_velho = i
    
    if sexos[i] == 'F' and idades[i] < 20:
        mulheres_jovens += 1
    

print(f'\nA média de idade do grupo é de {soma_idades / 4}')
print(f'O homem mais velho tem {idades[mais_velho]} e se chama {nomes[mais_velho]}')
print(f'Ao todo são {mulheres_jovens} mulheres com menos de 20 anos')

