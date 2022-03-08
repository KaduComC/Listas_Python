# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
# Os códigos utilizados são:

#     1 , 2, 3, 4  - Votos para os respectivos candidatos 
#     (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#     5 - Voto Nulo
#     6 - Voto em Branco

#     Faça um programa que calcule e mostre:
#     O total de votos para cada candidato;
#     O total de votos nulos;
#     O total de votos em branco;
#     A percentagem de votos nulos sobre o total de votos;
#     A percentagem de votos em branco sobre o total de votos. 
#     Para finalizar o conjunto de votos tem-se o valor zero. 
total = qt1 = qt2 = qt3 = qt4 = qt5 = qt6 = 0

cont = False
i = 1

print('1 - José\n2 - João\n3 - Jaime\n4 - Jonas\n5 - Voto nulo\n6 - Voto em Branco\n0 - Sair')


while cont == False:
    op = int(input(f'Eleitor {i}, informe seu canditato: '))
    if op == 1:
        qt1 += 1
    elif op == 2:
        qt2 += 1
    elif op == 3:
        qt3 += 1
    elif op == 4:
        qt4 += 1
    elif op == 5:
        qt5 += 1
    elif op == 6:
        qt6 += 1
    elif op == 0:
        cont = True
    else:
        print('Opção inválida')
    i += 1

total = qt1 + qt2 + qt3 + qt4 + qt5 + qt6
print(total)
