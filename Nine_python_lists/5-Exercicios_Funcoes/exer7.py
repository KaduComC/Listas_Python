# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma 
# prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o 
# número de dias em atraso e passar estes valores para a função valorPagamento, que 
# calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela. Após a execução o 
# programa deverá voltar a pedir outro valor de prestação e assim continuar até 
# que seja informado um valor igual a zero para a prestação. Neste momento o programa 
# deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor 
# total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. 
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de 
# multa, mais 0,1% de juros por dia de atraso.
def valor_pagamento(valor_pago, dias_atraso):
    if dias_atraso == 0:
        return valor_pago 
    else:
        juros_dia = 0.1 * dias
        return valor_pago + ((valor_pago * 0.03) + juros_dia)

valor_prestacao = 1
relatorio = []

while valor_prestacao != 0:
    valor_prestacao = float(input('\nInforme o valor a ser pago: '))
    if valor_prestacao == 0:
        break
    dias = int(input('Informe a quantidade de dias de atraso: '))

    val = valor_pagamento(valor_prestacao, dias)

    print(f'Valor: {val}')

    relatorio.append(val)

    print('Informe 0 no valor para sair')

print('\nRelatório')
for i in relatorio:
    print(i)
print(f'\nValor total do dia, onde teve {len(relatorio)} entradas, é de: {sum(relatorio)}')