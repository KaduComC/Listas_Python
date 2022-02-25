# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

#     Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#     Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#     A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do 
# percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
sal = 1000 + (1000 * 0.015)
print(f'1995 - R$ 1000,00')
print(f'1996 - R$ {round(sal, 2)}')
for i in range(1997, 2022 + 1):
    reaj = sal + (sal * (0.015 * 2) )
    sal = reaj
    print(f'{i} - R$ {round(reaj, 2)}')