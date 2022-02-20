# Faça um programa para a leitura de duas notas parciais de um aluno. O programa 
# deve calcular a média alcançada por aluno e apresentar:

#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez. 
notas = []
for i in range(2):
    notas.append(int(input(f'{i + 1} nota: ')))

media = sum(notas) / 2
if media == 10:
    print('Aprovado com Distinção')
elif media < 10 and media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')