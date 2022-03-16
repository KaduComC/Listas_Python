# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota = []

for i in range(1, 4 + 1):
    nota.append(float(input(f'Informe a {i} nota: ')))

media = sum(nota) / 4
print(f'Media: {media}')