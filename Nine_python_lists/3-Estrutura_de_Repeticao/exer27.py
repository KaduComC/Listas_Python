# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos. 
qtd_tur = int(input('Informe a quantidade de turmas: '))

alunos = []

for i in range(1, qtd_tur + 1):
    qtd_alunos = int(input(f'Informe a quantidade de alunos da {i} turma: '))

    while qtd_alunos > 40:
        print('A turma não pode ter mais de 40 alunos')
        qtd_alunos = int(input(f'Informe a quantidade de alunos da {i} turma novamente: '))
    
    alunos.append(qtd_alunos)

media = sum(alunos) / qtd_tur
print(f'O número médio de alunos por turma é {media}')