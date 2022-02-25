# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que 
# leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior 
# temperaturas informadas, bem como a média das temperaturas. 
temps = []
cont = False
while cont == False:
    temp = int(input('Informe a temperatura: '))
    temps.append(temp)

    op = str(input('Deseja continuar?[S/n]\nResponda: ')).lower()
    if op == 's':
        cont = False
    elif op == 'n':
        cont = True
    else:
        print('Opção inválida')

print(f'Maior temperatura: {max(temps)}\nMenor temperatura: {min(temps)}')