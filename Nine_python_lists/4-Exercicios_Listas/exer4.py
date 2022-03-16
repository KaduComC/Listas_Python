# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
#  Imprima as consoantes.

vogais = ['a', 'e', 'i', 'o', 'u']
caracteres = []
consoante = []
cont = 0
i = 1

while i <= 10:
    carac = str(input(f'Informe o {i} caracter: '))
    caracteres.append(carac)
    i += 1

    if carac not in vogais:
        cont += 1
        consoante.append(carac)

print((len(caracteres)) - cont)
print(consoante)