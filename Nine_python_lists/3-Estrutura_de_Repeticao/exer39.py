# Faça um programa que leia dez conjuntos de dois valores, o primeiro 
# representando o número do aluno e o segundo representando a sua altura em centímetros. 
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número 
# do aluno mais baixo, junto com suas alturas. 
numero_aluno_alto = 0
numero_aluno_baixo = 0
 
aluno_alto = 0
aluno_baixo = 200

for i in range(1, 10 + 1):
    altura = int(input(f'Informe a altura do aluno {i} em cm: '))

    if altura > aluno_alto:
        aluno_alto = altura
        numero_aluno_alto = i

    if altura < aluno_baixo:
        aluno_baixo = altura
        numero_aluno_baixo = i

print(f'\nAluno {numero_aluno_alto} é o mais alto, com {aluno_alto}cm' +
    f'\nAluno {numero_aluno_baixo} é o mais baixo, com {aluno_baixo}cm')