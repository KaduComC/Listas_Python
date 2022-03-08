# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os 
# seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

#     Os juros e a quantidade de parcelas seguem a tabela abaixo:

#     Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#     1       0
#     3       10
#     6       15
#     9       20
#     12      25

#     Exemplo de saída do programa:

#     Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#     R$ 1.000,00     0               1                       R$  1.000,00
#     R$ 1.100,00     100             3                       R$    366,00
#     R$ 1.150,00     150             6                       R$    191,67
divida = float(input('Informe o valor da divida: '))
print('\nValor da Dívida || Valor dos Juros || Quantidade de Parcelas || Valor da Parcela')

for i in range(1, 5 + 1):
    parcela = 0
    if i == 1:
        parcela = 1
        juros = 0
    
    elif i == 2:
        parcela = 3
        juros = 0.1
    
    elif i == 3:
        parcela = 6
        juros = 0.15

    elif i == 4:
        parcela = 9
        juros = 0.20

    elif i == 5:
        parcela = 12
        juros = 0.25
    
    print(f'R$ {round(divida + (divida * juros), 2)}', end = '          ')
    print(f'{int(divida * juros)}', end = '                  ')
    print(f'{parcela}', end = '                         ')
    print(f'R$ {round((divida + (divida * juros)) / parcela, 2)}')