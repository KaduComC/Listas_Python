# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros 
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em 
# porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.
def soma_imposto(taxa_imposto, custo):
    altera = custo + (custo * (taxa_imposto / 100))
    print(f'O valor com impostos: {altera}')

taxa = int(input('Informe a taxa de imposto: '))
valor = float(input('Informe a valor do produto: '))

soma_imposto(taxa, valor)