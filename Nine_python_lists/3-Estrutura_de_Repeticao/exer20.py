# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. 
continuar = False

while continuar == False:
    n = int(input('Informe o valor para calcular o fatorial: '))
    fat = 1
    
    if n > 0 and n <= 16:
        for i in range(1, n + 1):
            fat *= i
        print(f'Fatorial de {n}! é {fat}')
    else:
        print('Valor tem que ser positivo maio que zero oe menor ou igual a 16')

    op = str(input('Deseja continuar?[S/n]\nResponda: '))
    
    if op == 's':
        continuar = False
    elif op == 'n':
        continuar = True
    else:
        print(f'Invalid op')