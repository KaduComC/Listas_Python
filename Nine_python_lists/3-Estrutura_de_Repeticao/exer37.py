# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais 
# alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um 
# programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
# do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes 
cod_alto = 0
cod_baixo = 0

cod_gordo = 0
cod_magro = 0

altura = []
maior_altura = 1.20
menor_altura = 2.70

peso = []
mais_gordo = 20
mais_magro = 1000

cod = 1

while True:
    cod = int(input('\nInforme o código: '))
    if cod == 0:
        break
    else:
        at = float(input('Altura: '))
        altura.append(at)

        ps = float(input('Peso: '))
        peso.append(ps)

        if at > maior_altura:
            maior_altura = at
            cod_alto = cod
        if at < menor_altura:
            menor_altura = at
            cod_baixo = cod

        if ps > mais_gordo:
            mais_gordo = ps
            cod_gordo = cod
        if ps < mais_magro:
            mais_magro = ps
            cod_magro = cod

print(f'\nMaior altura: {maior_altura} ----- cod {cod_alto}' +
    f'\nMenor altura: {menor_altura} ----- cod {cod_baixo}' +
    f'\nMais gordo: {mais_gordo} ----- cod {cod_gordo}' +
    f'\nMais magro: {mais_magro} ----- cod {cod_magro}' +
    f'\nMédia altura: {sum(altura) / len(altura)}' +
    f'\nMédia peso: {sum(peso) / len(peso)}')

# Há outras formas masi faceis de fazer esse exercicio, mas quis fazer desta forma