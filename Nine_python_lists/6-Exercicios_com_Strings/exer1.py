# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas 
# seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento 
# e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
def acoes(string1, string2):
    if len(string1) == len(string2):
        print('\nAs duas strings são do mesmo tamanho.')
    else:
        print('As duas strings são de tamanhos diferentes.')

    if string1 == string2:
        print('\nAs duas strings possuem o mesmo conteúdo.')
    else:
        print('As duas strings possuem conteúdo diferente.')

def tamanho(string1, string2):
    print(f'Tamanho de "{string1}": {len(string1)} caracteres')
    print(f'Tamanho de "{string2}": {len(string2)} caracteres')

string1 = str(input('Informe a primeira frase: '))
string2 = str(input('Informe a segunda frase: '))

st1 = string1.lower()
st2 = string2.lower()

print('Compara duas strings')

print(f'\nString 1: {string1}')
print(f'String 1: {string1}')

tamanho(st1, st2)
acoes(st1, st2)