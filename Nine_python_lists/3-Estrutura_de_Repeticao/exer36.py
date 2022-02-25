# Desenvolva um programa que faça a tabuada de um número qualquer inteiro 
# que será digitado pelo usuário, mas a tabuada não deve necessariamente 
# iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
# também pelo usuário, conforme exemplo abaixo:

#     Montar a tabuada de: 5
#     Começar por: 4
#     Terminar em: 7

#     Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#     5 X 4 = 20
#     5 X 5 = 25
#     5 X 6 = 30
#     5 X 7 = 35

tab = int(input('Informe qual o valor da tabuada: '))
start = int(input('Informe por qual valor deve começar: '))
end = int(input('Informe até que valor a tabuada deve ir: '))

if end < start:
    print('Inválido')
else:
    for i in range(start, end + 1):
        print(f'{tab} X {i} = {tab * i}')