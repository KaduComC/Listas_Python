# Faça um programa que leia uma quantidade indeterminada de números positivos e 
# conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo. 
int1 = 0
int2 = 0
int3 = 0
int4 = 0
cont = 1
while True:
    valor = int(input(f'Informe o {cont} valor: '))
    if valor >= 0:
        if valor >= 0 and valor <= 25:
            int1 += 1
        elif valor > 25 and valor <= 50:
            int2 += 1
        elif valor > 50 and valor <= 75:
            int3 += 1
        elif valor > 75 and valor <= 100:
            int4 += 1
        else:
            print('Valor não existe nos intervalos: [0 - 25], [26 - 50], [51 - 75] e [76 - 100]')
    else:
        break
    cont += 1

print(f'Existem {int1} números no intervalo [0 - 25]')
print(f'Existem {int2} números no intervalo [26 - 50]')
print(f'Existem {int3} números no intervalo [51 - 75]')
print(f'Existem {int4} números no intervalo [76 - 100]')