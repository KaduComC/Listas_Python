# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a 
# soma dos quadrados dos elementos do vetor.
vet_normal = []
vet_quadrado = []

for i in range(1, 10 + 1):
    vet_normal.append(int(input(f'Informe o {i} valor: ')))

for i in vet_normal:
    vet_quadrado.append(i ** 2)

print(sum(vet_quadrado))