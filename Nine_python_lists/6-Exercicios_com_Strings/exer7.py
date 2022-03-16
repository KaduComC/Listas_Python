# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário 
# (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.
vog = ['a', 'e', 'i', 'o', 'u']

frase = str(input('Informe a frase: '))

espaco = frase.count(' ')
voga = frase.count('a')
voge = frase.count('e')
vogi = frase.count('i')
vogo = frase.count('o')
vogu = frase.count('u')

print(f'Quantidade de espaços: {espaco}')
print(f'Quantidade de a: {voga}')
print(f'Quantidade de e: {voge}')
print(f'Quantidade de i: {vogi}')
print(f'Quantidade de o: {vogo}')
print(f'Quantidade de u: {vogu}')
