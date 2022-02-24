# aça um programa que, dado um conjunto de N números, determine o menor 
# valor, o maior valor e a soma dos valores. 
n = int(input('Quantos valores o conjunto terá: '))
soma = 0
x = []


for i in range(1, n + 1):
    val = int(input(f'{i} valor: '))
    x.append(val)

media = sum(x) / n
print('Média = ', media)
print('Maior = ', max(x))
print('Menor = ', min(x))