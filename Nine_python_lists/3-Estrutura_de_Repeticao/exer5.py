# Altere o programa anterior permitindo ao usuário informar as populações e as 
# taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação. 
anos = 0
a = int(input('A: '))
b = int(input('B: '))
taxa_a = float(input('Taxa de crescimento da cidade A: '))
taxa_b = float(input('Taxa de crescimento da cidade B: '))
taxa_a = taxa_a / 100
taxa_b = taxa_b / 100

while a < b:
    a = a + (a * taxa_a)
    b = b + (b * taxa_b)
    anos += 1

print(f'A cidade A precisará de {anos} anos para igualar ou ultrapassar a cidade B')