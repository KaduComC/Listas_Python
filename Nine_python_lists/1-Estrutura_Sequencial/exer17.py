# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da 
# tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 
# situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
metros2 = int(input('Metros quadrados: '))
litros = metros2 / 6
latas = litros / 18
galoes = litros / 3.6

print(f'Serão usaddas {latas:,.0f}\nO total a ser pago em litros será de R${round(latas) * 80}'+
    f'\nO total a ser pago em galões será de R${round(galoes) * 25}')