# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um 
# valor n inteiro imprima até a n-ésima linha.
def rep(n):
    for i in range(1, n):
        print(i)
        i += 1
    
n = 5
rep(n)