# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vet = []

for i in range(1, 5 + 1):
    vet.append(int(input(f'Informe o {i} valor inteiro: ')))

print(vet)