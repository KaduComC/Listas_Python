# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

#     Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#     Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#     A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do 
# percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do 
# funcionário. 
val = float(input('Informe seu salário: '))
sal = val + (val * 0.015)
print(f'\nSalario no ano de 1995 é R$ {round(val, 2)}')
print(f'Salario no ano de 1996 é R$ {round(sal, 2)}')
for i in range(1997, 2022 + 1):
    reaj = sal + (sal * (0.015 * 2) )
    sal = reaj
    print(f'Salario no ano de {i} é R$ {round(reaj, 2)}')