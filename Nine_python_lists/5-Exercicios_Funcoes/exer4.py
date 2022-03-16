# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu 
# argumento for zero ou negativo.
def valor(n):
    if n > 0:
        print('P')
    elif n <= 0:
        print('N')
    
n = int(input('Informe um valor: '))
valor(n)