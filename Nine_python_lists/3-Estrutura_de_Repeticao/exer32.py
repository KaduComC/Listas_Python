# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

#     Fatorial de: 5
#     5! =  5 . 4 . 3 . 2 . 1 = 120
valor = int(input('Informe o valor para calcular o fatorial: '))
cont = valor
fat = 1

print(f'{valor}! = ', end = '')
while cont > 0:
    print(f'{cont} ', end = '')
    print(f' x ' if cont > 1 else ' = ', end = '')
    fat *= cont
    cont -= 1

print(f'{fat}')
