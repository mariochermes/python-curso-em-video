def cabe�alho(msg):
    tam = len(msg) + 8
    print('�' * tam)
    print(f'{msg:^{tam}}')
    print('�' * tam)