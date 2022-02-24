# Faça um programa que leia e valide as seguintes informações:

#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd'; 
nome = str(input('Nome: '))
while len(nome) <= 3:
    nome = str(input('Nome: '))

idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade: '))

salario = float(input('Salario: '))
while salario < 0:
    salario = float(input('Salario: '))

sexo = str(input('Sexo: ')).lower()
while sexo != 'f' and sexo != 'm':
    sexo = str(input('Sexo: ')).lower()

estado_civel = str(input('Estado Civil: ')).lower()
while estado_civel != 's' and estado_civel != 'c' and estado_civel != 'v' and estado_civel != 'd':
    estado_civel = str(input('Estado Civil: ')).lower()