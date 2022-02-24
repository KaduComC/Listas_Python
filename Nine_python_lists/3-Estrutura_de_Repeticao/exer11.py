# Altere o programa anterior para mostrar no final a soma dos números. 
start = int(input('Primeiro valor: '))
stop = int(input('Segundo valor: '))
soma = 0
if start >= stop:
    print('Valores inválidos')
else:
    for i in range(start + 1, stop):
        print(i)
        soma += i

print('Soma = ', soma)