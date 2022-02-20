# Faça um programa que pergunte o preço de três produtos e informe qual 
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
preco = []
for i in range(3):
    preco.append(float(input(f'{i + 1} preço: ')))

preco.sort()
print(f'Você deve comprar o produto com valor de: {preco[0]}')