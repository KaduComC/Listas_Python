# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e 
# gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4

# [Endereços inválidos:]
# 257.32.4.5
# ,85.345.1.2
# ,9.8.234.5
# ,192.168.0.256
import re

def valida_re():
    return '^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])'

def valida_ip(ip):
    if(re.search(valida_re(), ip)):
        with open('7-Exercicios_Arquivos/ip_validos.txt', 'a') as arquivo_novo:
            arquivo_novo.writelines(ip)
            arquivo_novo.writelines('\n')
    else:
        with open('7-Exercicios_Arquivos/ip_invalidos.txt', 'a') as arquivo_novo:
            arquivo_novo.writelines(ip)
            arquivo_novo.writelines('\n')

with open('7-Exercicios_Arquivos/ips.txt', 'r') as arquivo:
    ips = arquivo.readline()
    ipsl = list(map(str, ips.split()))

for i in ipsl:
    valida_ip(i)

def separa_ips():
    print('Endereços válidos:')
    with open('7-Exercicios_Arquivos/ip_validos.txt', 'r') as arquivo_novo:
        vl = arquivo_novo.read()
        print(vl)

    print('\nEndereços inválidos:')
    with open('7-Exercicios_Arquivos/ip_invalidos.txt', 'r') as arquivo_novo:
        il = arquivo_novo.read()
        print(il)

separa_ips()