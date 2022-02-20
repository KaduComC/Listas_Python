# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
# ou "Valor Inválido!", conforme o caso. 
turno = str(input('Qual turno você estuda?\n'+
    'M - matutino\nV - Vespertino\nN - Noturno\nR: ')).lower()
if turno == 'm': print('Bom Dia!')
elif turno == 'v': print('Boa Tarde!')
elif turno == 'n': print('Boa Noite!')
else: print('Valor Inválido!')