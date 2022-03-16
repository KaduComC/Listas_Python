# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
# gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
#  Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai 
# utilizar o sistema. Após todos os alunos terem respondido informar:
#     Maior e Menor Acerto;
#     Total de Alunos que utilizaram o sistema;
#     A Média das Notas da Turma.
#     Gabarito da Prova:
#     01 - A
#     02 - B
#     03 - C
#     04 - D
#     05 - E
#     06 - E
#     07 - D
#     08 - C
#     09 - B
#     10 - A
#     Após concluir isto você poderia incrementar o programa permitindo que o professor 
# digite o gabarito da prova antes dos alunos usarem o programa. 
print('Informe as respostas da prova\n\n')
continuar = True
nota = 0

while continuar == True:
    for i in range(1, 10 + 1):
        qt = str(input(f'Resposta da questão 0{i}: ')).lower()
        
        if i == 1:
            if qt == 'a': nota += 1
        
        if i == 2:
            if qt == 'b': nota += 1

        if i == 3:
            if qt == 'c': nota += 1
        
        if i == 4:
            if qt == 'd': nota += 1
        
        if i == 5:
            if qt == 'e': nota += 1
        
        if i == 6:
            if qt == 'e': nota += 1

        if i == 7:
            if qt == 'd': nota += 1

        if i == 8:
            if qt == 'c': nota += 1

        if i == 9:
            if qt == 'b': nota += 1

        if i == 10:
            if qt == 'a': nota += 1

            
