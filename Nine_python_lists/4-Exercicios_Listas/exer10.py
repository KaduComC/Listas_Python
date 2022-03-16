# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
# compostos pelos elementos intercalados dos dois outros vetores.
vet_1 = []
vet_2 = []
vet_3 = []

for i in range(1 , 10 + 1):
    vet_1.append(int(input(f'Informe o {i} valor do primeiro vetor: ')))
    vet_2.append(int(input(f'Informe o {i} valor do segundo vetor: ')))

for x in range(0, 10):
    vet_3.append(vet_1[x])
    vet_3.append(vet_2[x])

print(vet_3)