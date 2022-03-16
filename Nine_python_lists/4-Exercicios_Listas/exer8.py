# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada 
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idade = []
altura = []

for i in range(5):
    idade.append(int(input(f'Informe a {i+1} idade: ')))
    altura.append(int(input(f'Informe a {i+1} altura: ')))

print(f'Idade inversa')
for i in range(5):
    print(f'Idade: {idade[len(idade)-1-i]}')

print('Altura inversa')
for x in altura:
    print(f'Altura: {altura[len(altura)-1-x]}')
