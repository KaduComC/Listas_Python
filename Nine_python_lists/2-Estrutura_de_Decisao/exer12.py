# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
# são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
# Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é
# descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
# quantidade de horas trabalhadas no mês.
#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
hora_valor = float(input('Informe o valor da hora: '))
qtd_hora = int(input('Informe a quantidade de horas trabalhadas no mês: '))
sal_bruto = hora_valor * qtd_hora

des_ir = ''
des_IR = 0

if sal_bruto <= 900:
    des_ir = 'Isento'
elif sal_bruto > 900 and sal_bruto <= 1500:
    des_IR = sal_bruto * 0.05
    des_ir = f'IR 5%:                      R$ {des_IR}'
elif sal_bruto > 1500 and sal_bruto <= 2500:
    des_IR = sal_bruto * 0.1
    des_ir = f'IR 10%:                     R$ {des_IR}'
elif sal_bruto > 2500:
    des_IR = sal_bruto * 0.2
    des_ir = f'IR 20%:                     R$ {des_IR}'

sindicato = sal_bruto * 0.03
fgts = sal_bruto * 0.11
total = sindicato + fgts + des_IR

sal_liquido = sal_bruto - total
print(f'Salário Bruto:              R$ {sal_bruto}')
print(f'{des_ir}')
print(f'Sindicato:                  R$ {sindicato}')
print(f'FGTS:                       R$ {fgts}')
print(f'Total de descontos:         R$ {total}')
print(f'Salário Liquido:            R$ {sal_liquido}')