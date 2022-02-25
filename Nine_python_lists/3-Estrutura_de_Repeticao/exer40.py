# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de 
# trânsito. Foram obtidos os seguintes dados:

#     Código da cidade;
#     Número de veículos de passeio (em 1999);
#     Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#     Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#     Qual a média de veículos nas cinco cidades juntas;
#     Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. 
maior_codigo = 0
menor_codigo = 0

maior_indice = 0
menor_indice = 999999

num_veiculos = []
num_acidentes = []


for i in range(1, 5 + 1):
    veiculos = int(input(f'\nInforme o número de veículos da {i} cidade: '))
    num_veiculos.append(veiculos)

    acidentes = int(input(f'Informe o número de acidentes da {i} cidade: '))
    if veiculos < 2000:
        num_acidentes.append(acidentes)

    if acidentes > maior_indice:
        maior_indice = acidentes
        maior_codigo = i

    if acidentes < menor_indice:
        menor_indice = acidentes
        menor_codigo = i

print(f'\nMaior indice de acidentes pertence a cidade {maior_codigo}, com indice de {maior_indice} de acidentes')
print(f'Menor indice de acidentes pertence a cidade {menor_codigo}, com indice de {menor_indice} de acidentes')
print(f'A média dde veiculos das 5 cidades é de {sum(num_veiculos) / 5}')
print(f'A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de {sum(num_acidentes) / len(num_acidentes)}')