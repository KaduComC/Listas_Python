# Faça um programa que peça para n pessoas a sua idade, ao final o 
# programa devera verificar se a média de idade da turma varia 
# entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, 
# adulta ou idosa, conforme a média calculada. 
continuar = False
pessoas = []
cont = 0

while continuar == False:
    idade = int(input('Idade: '))
    pessoas.append(idade)

    op = str(input('Adicionar mais idade?[S/n/\nResponda: ')).lower()
    if op == 's':
        continuar = False
    elif op == 'n':
        continuar = True
    else:
        print('Opção inválida')
    cont += 1

media = sum(pessoas) / cont

if media >= 0 and media <= 25:
    print('A turma é jovem')
elif media > 25 and media <= 60:
    print('A turma é adulta')
elif media > 60:
    print('A turma é idosa')