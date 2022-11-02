seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
        print('equilátero')
    elif seg1 != seg2 != seg3 != seg1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo')