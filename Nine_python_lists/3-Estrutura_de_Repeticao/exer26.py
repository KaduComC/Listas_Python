# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. 
total_eleitores = int(input('\nInforme o total de eleitores: '))
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

for i in range(1, total_eleitores + 1):
    print(f'\n\n{i} eleitor escolha seu canditado:')
    print('\nDigite 1 para Primeiro candidato')
    print('Digite 2 para Segundo candidato')
    print('Digite 3 para Terceiro candidato')
    op = int(input('Escolha: '))
    if op == 1:
        candidato_1 += 1
    elif op == 2:
        candidato_2 += 1
    elif op == 3:
        candidato_3 += 1
    else:
        print('candidato inexistente')

print(total_eleitores)
print(f'Primeiro candidato recebeu {candidato_1} votos' +
    f'\nSegundo candidato recebeu {candidato_2} votos' +
    f'\nTerceiro candidato recebeu {candidato_3} votos')