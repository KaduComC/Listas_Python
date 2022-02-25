# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais 
# alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um 
# programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
# do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes 
code = []
altura = []
peso = []

pessoas = {}

cod_mais_alto = 0
codigo = 1
cont = 0

print('Informe 0 para parar o registro\n')

while codigo == 1:
    cod = int(input('\nCódigo: '))
    if cod == 0:
        break

    at = float(input('Altura: '))
    ps = float(input('Paso: '))

    code.append(cod)
    altura.append(at)
    peso.append(ps)
    cont += 1
    pessoas[cod] = [at, ps]

media_altura = sum(altura) / cont
media_peso = sum(peso) / cont
print(f'Maior altura: {max(altura)}' +
    f'\nMenor altura: {min(altura)}' +
    f'\nMaior peso: {max(peso)}' +
    f'\nMenor peso: {min(peso)}' +
    f'\nMedia altura: {media_altura}' +
    f'\nMedia peso: {media_peso}')
# ATUALIZAR