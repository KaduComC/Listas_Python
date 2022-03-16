# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.
vet20 = []
vetP = []
vetI = []


for i in range(1, 20 + 1):
    vet20.append(int(input(f'Informe o {i} valor: ')))

for x in vet20:
    if x % 2 == 0: vetP.append(x)
    elif x % 2 == 1: vetI.append(x)

print(f'\nValores: {vet20}')
print(f'\nValores pares: {vetP}')
print(f'\nValores impares: {vetI}')