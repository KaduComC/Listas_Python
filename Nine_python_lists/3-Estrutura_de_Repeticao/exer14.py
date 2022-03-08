# Faça um programa que peça 10 números inteiros, calcule e mostre a 
# quantidade de números pares e a quantidade de números impares. 
from re import I

par = 0
impar = 0

for i in range(1, 10 + 1):
    num = int(input(f'{i} valor: '))
    if num % 2 == 0:
        par += 1
    elif num % 2 == 1:
        impar += 1

print(f'Quantidade de pares: {par}\nQuantidade de impares: {impar}')