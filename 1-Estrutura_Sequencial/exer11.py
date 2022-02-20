# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo. 
int1 = int(input('Primeiro valor inteiro: '))
int2 = int(input('Segundo valor inteiro: '))
real = float(input('Um valor real: '))
print(f'Op1 = {(int1 * 2) + (int2 / 2)}\nOp2 = {(int1 * 3) + int2}\nOp3 = {real**3}')