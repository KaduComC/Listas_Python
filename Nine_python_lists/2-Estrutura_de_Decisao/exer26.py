# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#     a Álcool:
#     b até 20 litros, desconto de 3% por litro
#     c acima de 20 litros, desconto de 5% por litro
#     d Gasolina:
#     e até 20 litros, desconto de 4% por litro
#     f acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o 
#       número de litros vendidos, o tipo de combustível (codificado da seguinte forma: 
#       A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o 
#       preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
tipo = str(input('Qual tipo de combustível?[A -  alcool / G - gasolina]: ')).lower()
litros = int(input('Quantos litros: '))

if tipo == 'a':
    if litros <= 20:
        valor = litros * 1.99
        desconto = valor - (valor * 0.03)
        print(f'Valor pago por {litros} de álcool será de R${desconto}')
    elif litros > 20:
        valor = litros * 1.99
        desconto = valor - (valor * 0.05)
        print(f'Valor pago por {litros} de álcool será de R${round(desconto)}')
elif tipo == 'g':
    if litros <= 20:
        valor = litros * 2.50
        desconto = valor - (valor * 0.04)
        print(f'Valor pago por {litros} de gasolina será de R${desconto}')
    elif litros > 20:
        valor = litros * 2.50
        desconto = valor - (valor * 0.06)
        print(f'Valor pago por {litros} de gasolina será de R${desconto}')