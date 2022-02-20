# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
# dezenas e unidades do mesmo.
#     Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#     326 = 3 centenas, 2 dezenas e 6 unidades
#     # 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 
# 25, 20, 10, 21, 11, 1, 7 e 16 
num = str(input('Informe um valor: '))
qt = len(num)
if int(num) < 1000:
    if qt == 3:
        a, b, c = map(int, num)
        print(f'{a} centenas, {b} dezenas e {c} unidades')
    elif qt == 2:
        a, b = map(int, num)
        print(f'{a} dezenas e {b} unidades')
    elif qt == 1:
        print(f'{num} unidades')
else:
    print('Valor inválido')