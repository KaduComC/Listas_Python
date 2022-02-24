# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o 
# usuário informe um valor válido. 
nota = int(input('Um nota de 0 a 10: '))
if nota < 0 or nota > 10:
    print('Valor inválido')
while nota < 0 or nota > 10:
    nota = int(input('Um nota de 0 a 10: '))
    if nota < 0 or nota > 10:
        print('Valor inválido')
        continue
    else: 
        print('Valor válido')
        break