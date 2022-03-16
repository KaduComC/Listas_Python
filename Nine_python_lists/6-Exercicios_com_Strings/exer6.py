# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do 
# usuário e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.
def mes(m):
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 
        7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
    if m >= 1 and m <= 12:
        return meses[m]
    else:
        return 'null'

d = int(input('Dia do nascimento: '))
m = int(input('Mes de nascimento: '))
a = int(input('Ano de nascimento: '))

print(f'Data de nascimento: {d}/{m}/{a}')
print(f'Você nasceu em {d} de {mes(m)} de {a}')
