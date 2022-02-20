# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando 
# ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o 
# programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. 
# Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
values = input('Informe os valores de a, b e c respectivamente: ').split()
a, b, c = map(int, values)

if a == 0:
    print('Não é equcação de segundo grau')
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('A equação não possui raizes reais')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'A equação possui apenas uma raiz real\nResultado: {x}')
    elif delta > 0:
        x1 = -b + delta**2/ (2 * a)
        x2 = -b - delta**2/ (2 * a)
        print(f'A equação possui duas raiz reais\nResult: x1 = {x1}, x2 = {x2}')
