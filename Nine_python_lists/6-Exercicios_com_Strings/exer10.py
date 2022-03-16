# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um 
# número até 99 e imprima-o na tela por extenso.
from num2words import num2words as nw

num = int(input('Informe um valor: '))

print(nw(num, lang='pt_BR').capitalize())