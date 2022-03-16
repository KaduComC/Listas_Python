# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada 
# seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F
nome = str(input('Informe o nome: '))

for i in range(0, len(nome) + 1):
    print(nome[i:].upper())

# ou
print('\n\n')

cont = len(nome)
while cont > 0:
    print(nome[:cont].upper())
    cont -= 1