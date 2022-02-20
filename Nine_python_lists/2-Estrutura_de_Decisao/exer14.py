# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
# de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
nt1 = float(input('Informe a primeira nota: '))
nt2 = float(input('Informe a segunda nota: '))

print('Media de Aproveitamento ------ Conceito')

media = (nt1 + nt2) / 2
if media >= 0 and media < 4:
    print(f'Media = {media}             ------      E')
elif media >= 4 and media < 6:
    print(f'Media = {media}             ------      D')
elif media >= 6 and media < 7.5:
    print(f'Media = {media}             ------      C')
elif media >= 7.5 and media < 9:
    print(f'Media = {media}             ------      B')
elif media >= 9 and media < 10:
    print(f'Media = {media}             ------      A')