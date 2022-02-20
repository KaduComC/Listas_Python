# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
ganho_hora = float(input('Ganho por hora: '))
hora_mes = int(input('Hora por mes: '))
salario = ganho_hora * hora_mes

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

salario_liquido = salario - ir - inss - sindicato
print(
    f'Salário bruto: R${salario}\nINSS: R${inss}\nSindicato: R${sindicato}\nSalário líquido: R${salario_liquido}\n')