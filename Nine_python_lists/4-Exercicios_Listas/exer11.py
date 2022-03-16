# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
vet_1 = []
vet_2 = []
vet_3 = []
vet_4 = []

for i in range(1 , 10 + 1):
    vet_1.append(int(input(f'Informe o {i} valor do primeiro vetor: ')))
    vet_2.append(int(input(f'Informe o {i} valor do segundo vetor: ')))
    vet_3.append(int(input(f'Informe o {i} valor do terceiro vetor: ')))

for x in range(0, 10):
    vet_4.append(vet_1[x])
    vet_4.append(vet_2[x])
    vet_4.append(vet_3[x])

print(vet_4)