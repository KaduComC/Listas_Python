# Faça um programa que receba dois números inteiros e gere os 
# números inteiros que estão no intervalo compreendido por eles. 
start = int(input('Primeiro valor: '))
stop = int(input('Segundo valor: '))
if start >= stop:
    print('Valores inválidos')
else:
    for i in range(start + 1, stop):
        print(i)