# Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
# Dicas: 
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; 
# Triângulo Equilátero: três lados iguais; 
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes; 
values = input('Valores: ').split()
a, b, c = map(int, values)

if a + b > c and a + c > b and b + c > a:
    print('Não é um triangulo')
elif a == b and a == c:
    print('Equilátero')
elif a == b or b == c or c == a:
    print('Isósceles')
else: print('Escaleno')