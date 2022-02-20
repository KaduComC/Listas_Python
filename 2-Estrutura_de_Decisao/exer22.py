# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão). 
num = int(input('Valor: '))

if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é impar')