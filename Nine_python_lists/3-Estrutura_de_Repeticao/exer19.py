# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 
n = int(input('Quantos valores o conjunto terá: '))
soma = 0
x = []

for i in range(1, n + 1):
    val = int(input('Informe um valor: '))

    while val > 1000 or val < 0:
        val = int(input('Informe o valor outra vez: '))
    
    x.append(val)

media = sum(x) / n
print('Média = ', media)
print('Maior = ', max(x))
print('Menor = ', min(x))