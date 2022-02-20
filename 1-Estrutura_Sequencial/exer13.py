# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
#     Para homens: (72.7*h) - 58
#     Para mulheres: (62.1*h) - 44.7 
sexo = str(input('Seu sexo [F/M]: ')).lower()
h = float(input('Sua altura: '))

if sexo == 'f':
    print(f'Peso: {(62.1 * h ) - 44.7}')
elif sexo == 'm':
    print(f'Peso: {(72.7 * h) - 58}')
else:
    print('Opção errada')

