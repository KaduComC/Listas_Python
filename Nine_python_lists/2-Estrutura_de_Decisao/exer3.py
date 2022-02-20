# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
sexo = str(input('Sexo [F/M]: ')).lower()
if sexo == 'f': print('Feminino')
elif sexo == 'M': print('Masculino')
else: print('Sexo inválido')