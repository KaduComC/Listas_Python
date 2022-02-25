# Faça um programa que calcule o mostre a média aritmética de N notas. 
qtd_notas = int(input('Informe a quantidade de notas: '))
notas = []

for i in range(1, qtd_notas + 1):
    nota = float(input(f'Informe a {i} nota: '))
    notas.append(nota)

media = sum(notas) / qtd_notas
print(f'A média é: {media}')