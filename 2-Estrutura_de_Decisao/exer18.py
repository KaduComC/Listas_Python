# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
valido = False

mes_31 = [1, 3, 5, 7, 8, 10, 12]
mes_30 = [4, 6, 9, 11]

if mes in mes_31:
    if dia <= 31:
        valido = True
elif mes in mes_30:
    if dia <= 30:
        valido = True
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        if dia <= 29:
            valido = True
        elif dia <= 28:
            valido = True

if valido == True:
    print('Data válido')
else:
    print('Inválido')