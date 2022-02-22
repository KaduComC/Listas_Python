# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
#     ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
#     Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
#     quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
print('                      Até 5 Kg           Acima de 5 Kg')
print('Morango         R$ 2,50 por Kg          R$ 2,20 por Kg')
print('Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg')
kg_morango = int(input('Qantos quilos de morando: '))
kg_maca = int(input('Quantos quilos de maça: '))
kg_total = kg_morango + kg_maca    

valor_morango = 0
valor_maca = 0

if kg_morango <= 5:
    valor_morango = kg_morango * 2.50
else:
    valor_morango = kg_morango * 2.20

if kg_maca <= 5:
    valor_maca = kg_maca * 1.80
else:
    valor_maca = kg_maca * 1.50

valor_total = valor_morango + valor_maca

if kg_total > 8 or valor_total > 25: 
    print(f'Valor pago por {kg_morango}kg morango e {kg_maca}kg será de R${valor_total - (valor_total * 0.1)}')
else: 
    print(f'Valor pago por {kg_morango}kg morango e {kg_maca}kg será de R${valor_total}')