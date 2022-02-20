# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
vogais = ['a', 'e', 'i', 'o', 'u']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

letra = str(input('Letra: ')).lower()
if letra.isalpha():
    if letra in vogais:
        print('Vogal')
    else:
        print('Consoante')
else: 
    print('Inválido')