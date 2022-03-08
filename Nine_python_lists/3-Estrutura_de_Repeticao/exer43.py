# O cardápio de uma lanchonete é o seguinte:

#     Especificação   Código  Preço
#     Cachorro Quente 100     R$ 1,20
#     Bauru Simples   101     R$ 1,30
#     Bauru com ovo   102     R$ 1,50
#     Hambúrguer      103     R$ 1,20
#     Cheeseburguer   104     R$ 1,30
#     Refrigerante    105     R$ 1,00

#     Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado. 
print('Especificação   Código  Preço')
print('Cachorro Quente 100     R$ 1,20')
print('Bauru Simples   101     R$ 1,30')
print('Bauru com ovo   102     R$ 1,50')
print('Hambúrguer      103     R$ 1,20')
print('Cheeseburguer   104     R$ 1,30')
print('Refrigerante    105     R$ 1,00')

cont = False
valor = valor100 = valor101 = valor102 = valor103 = valor104 = valor105 = 0
qtd100 = qtd101 = qtd102 = qtd103 = qtd104 = qtd105 = 0

while cont == False:
    op = int(input('\nInforme o código do lanche: '))

    if op == 100:
        qtd100 = int(input('Informe a quantidade de Cachorro Quente: '))

    elif qtd101 == 101:
        qtd = int(input('Informe a quantidade de Bauru Simples: '))

    elif op == 102:
        qtd102 = int(input('Informe a quantidade de Bauru com ovo: '))

    elif op == 103:
        qtd103 = int(input('Informe a quantidade de Hambúrguer: '))

    elif op == 104:
        qtd104 = int(input('Informe a quantidade de Cheeseburguer: '))

    elif op == 105:
        qtd105 = int(input('Informe a quantidade de Refrigerante: '))

    else:
        print('Código inexistente')

    op2 = str(input('\nDeseja encerrar?[S/n]\nResponda: ')).lower()
    if op2 == 's':
        cont = True
        break
    elif op2 == 'n':
        cont = False
        continue
    else: 
        print('Opção inválida')
        break 

valor = (qtd100 * 1.20) + (qtd101 * 1.30) + (qtd102 * 1.50) 
valor = valor + (qtd103 * 1.20) + (qtd104 * 1.30) + (qtd105 * 1.00)
 
print(f'\nCachorro Quente 100 R$ 1,20 x {qtd100} = {qtd100 * 1.20}')
print(f'Bauru Simples   101 R$ 1,30 x {qtd101} = {qtd101 * 1.30}')
print(f'Bauru com ovo   102 R$ 1,50 x {qtd102} = {qtd102 * 1.50}')
print(f'Hambúrguer      103 R$ 1,20 x {qtd103} = {qtd103 * 1.20}')
print(f'Cheeseburguer   104 R$ 1,30 x {qtd104} = {qtd104 * 1.30}')
print(f'Refrigerante    105 R$ 1,00 x {qtd105} = {qtd105 * 1.00}')
print(f'Total = R$ {valor}')