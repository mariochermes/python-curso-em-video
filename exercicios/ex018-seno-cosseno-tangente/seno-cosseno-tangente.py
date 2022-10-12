import math

angulo = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {angulo} tem o SENO de {math.sin(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {math.cos(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {math.tan(math.radians(angulo)):.2f}')