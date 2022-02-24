# Faça um programa que leia 5 números e informe a soma e a média dos números. 
soma = 0
media = 0
for i in range(5):
    num = int(input('Valor: '))
    soma += num

media = soma / 5
print(f'\nSoma = {soma}\nMédia = {media}')