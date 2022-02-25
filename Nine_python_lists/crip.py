import cryptocode 
key = 'wow'
str1 = cryptocode.encrypt('Teste 2 de criptografia', key)

str2 = cryptocode.decrypt(str1, key)
print('\n',str1)
print('\n',str2)