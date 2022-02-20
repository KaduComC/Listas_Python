# Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
nota = []
media = 0
for i in range(4):
    nota.append(float(input(f'Informe a {i + 1} nota: ')))
    media = sum(nota)

print(f'Media é: {media / 4}')