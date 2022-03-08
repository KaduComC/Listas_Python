# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

#     Exemplo:

#       12376489
#       => 98467321
num = int(input('Informe um valor inteiro: '))

for i in range(1, num + 1):
    print(i, end = '')

print(' => ', end = '')

for i in range(num, 0, -1):
    print(i, end = '')