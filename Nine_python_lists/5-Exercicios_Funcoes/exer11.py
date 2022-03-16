# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e 
# retorne NULL caso a data seja inválida.
# import num2word as num
from calendar import isleap
from num2words import num2words as num
import time

def mes(m):
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 
            7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
    if m >= 1 and m <= 12:
        return meses[m]
    else:
        return 'null'

def dia(d, m, a):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d >= 1 and d <= 31:
            return num(d, lang = 'pt_BR').capitalize()
        else:
            return 'null'
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d >= 1 and d <= 30:
            return num(d, lang = 'pt_BR').capitalize()
        else:
            return 'null'
    elif m == 2:
        if isleap(a):
            if d >= 1 and d <= 29:
                return num(d, lang = 'pt_BR').capitalize()
            else:
                return 'null'
        else: 
            if d >= 1 and d <= 28:
                return num(d, lang = 'pt_BR').capitalize()
            else:
                return 'null'

def ano(a):
    if a >= 1000 and a <= 3000:
        return num(a, lang = 'pt_BR').capitalize()
    else:
        return 'null'

d = int(input('Informe o dia: '))
m = int(input('Informe o mês: '))
a = int(input('Informe o ano: '))

print(f'\n{d}/{m}/{a}')

print(f'\n{dia(d, m, a)} de {mes(m)} de {ano(a)}')