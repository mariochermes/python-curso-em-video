def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if fim > início:
        for c in range(início, fim, passo):
            print(f'{c} ', end='')
        print()
    elif fim < início :
        for c in range(início, fim, -passo):
            print(f'{c} ', end='')
        print()
    else:
        print('Início e fim são íguais')


#Main
contador(1, 10, 1)
contador(10, 0, 2)
contador(10, 0, -2)
