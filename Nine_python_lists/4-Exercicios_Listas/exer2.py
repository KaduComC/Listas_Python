# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vet = []

for i in range(1, 10 + 1):
    vet.append(float(input(f'Informe o {i} valor real: ')))

print(vet)