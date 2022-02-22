# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#     Para atender a todos os clientes, cada cliente poderá levar apenas um 
# dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um 
# desconto de 5% sobre o total da compra. Escreva um programa que peça o 
# tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, 
# tipo de pagamento, valor do desconto e valor a pagar. 
print('                      Até 5 Kg           Acima de 5 Kg')
print('File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg')
print('Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
print('Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')

tipo = str(input('\nTipo de carne?\n[F - File Duplo / A - Alcatra / P - Picanha]\nEscolha: ')).lower()
kg = int(input('Quantidade em Kg: '))
cartao = str(input('Vai pagar no cartão Tabajara:\n[S/n]\nResponda: ')).lower()

valor = 0
resp = ''
if tipo == 'f' and kg <= 5:
    valor = kg * 4.90
    resp = f'File Duplo\nQuantidade: {kg}Kg\nPreço total: {valor}'
elif tipo == 'f' and kg > 5:
    valor = kg * 5.80
    resp = f'File Duplo\nQuantidade: {kg}Kg\nPreço total: {valor}'

if tipo == 'a' and kg <= 5:
    valor = kg * 5.90
    resp = f'Alcatra\nQuantidade: {kg}Kg\nPreço total: {valor}'
elif tipo == 'a' and kg > 5:
    valor = kg * 6.80
    resp = f'Alcatra\nQuantidade: {kg}Kg\nPreço total: {valor}'

if tipo == 'p' and kg <= 5:
    valor = kg * 6.90
    resp = f'Picanha\nQuantidade: {kg}Kg\nPreço total: {valor}'
elif tipo == 'p' and kg > 5:
    valor = kg * 7.80
    resp = f'Picanha\nQuantidade: {kg}Kg\nPreço total: {valor}'

if cartao == 's':
    des = valor * 0.05
    valor_des = valor - des
    print(f'Tipo de carne {resp}\nTipo do pagamento: Cartão Tabajara\nValor do desconto: {des}\nValor a pagar: {valor_des}')
elif cartao == 'n':
    print(f'Tipo de carne {resp}\nTipo do pagamento: Dinheiro\nValor a pagar: {valor}')