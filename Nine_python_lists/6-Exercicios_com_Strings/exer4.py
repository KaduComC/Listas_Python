# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome 
# em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO
nome = str(input('Informe o nome: '))

for i in range(0, len(nome) + 1):
    print(nome[:i].upper())