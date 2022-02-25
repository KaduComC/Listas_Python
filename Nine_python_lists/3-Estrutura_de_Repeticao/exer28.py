# Faça um programa que calcule o valor total investido por um colecionador em sua 
# coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a 
# quantidade de CDs e o valor para em cada um. 
qtd_cds = int(input('Informe a quantidade de CDs: '))
valor = []

for i in range(1, qtd_cds + 1):
    valor_cds = float(input(f'Valor do {i} CD: '))
    valor.append(valor_cds)

media = sum(valor) / qtd_cds
print(f'Valor total investido foi de R${sum(valor)}')
print(f'Valor médio dos CDs foi é de R${media}')