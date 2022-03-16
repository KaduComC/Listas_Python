# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
# a multiplicação e os números.
vet = []
mult = 1
for i in range(5):
    vet.append(int(input(f'Informe o {i+1} valor: ')))
    
for i in vet:
    mult *= i

print(sum(vet))
print(mult)
print(vet)
