# Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.
def soma(a, b, c):
    adicao = a + b + c
    print(f'A soma dos três argumentos é: {adicao}')

a = int(input('Primeiro argumento: '))
b = int(input('Segundo argumento: '))
c = int(input('Terceiro argumento: '))

soma(a, b, c)