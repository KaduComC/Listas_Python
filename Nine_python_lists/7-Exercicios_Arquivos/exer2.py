# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em 
# disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador 
# de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários 
# com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu 
# gerar o seguinte arquivo, chamado "usuarios.txt":

# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você 
# deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso 
# sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado 
# em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será 
# chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito 
# através de uma função, que será chamada pelo programa principal.

def conversao(dados):
    dados_ind = dados / (1024 * 1024)
    return round(dados_ind, 2)

def conversao_total(total):
    total_mega = total / (1024 * 1024)
    return total_mega

with open('7-Exercicios_Arquivos/usuarios.txt', 'r') as usuarios:
    linhas = usuarios.readlines()

usuario = []
dados_bytes = []
dados_megas = []
porcentagem = []

for i in linhas:
    l = i.split()
    usuario.append(l[0])
    dados_bytes.append(int(l[1]))

bytes = sum(dados_bytes)
total = conversao_total(bytes)

for i in dados_bytes: 
    dados_megas.append(conversao(i))

for i in dados_megas: 
    porcentagem.append((i / total) * 100)

with open('7-Exercicios_Arquivos/relátorio.txt', 'w') as relatorio:
    relatorio.write('ACME Inc.          Uso do espaço em disco pelos usuários')
    relatorio.write('\n-------------------------------------------------------------')
    relatorio.write('\nNr.  Usuário        Espaço utilizado     % do uso\n')
    
    for i in range(len(dados_bytes)):
        relatorio.write(f'\n{i + 1:<5}{usuario[i]:<15}{dados_megas[i]:<8} MB          {porcentagem[i]:.2f}%')
                            # 1         alexandre       434,99 MB             16,85%

    relatorio.write(f'\n\nEspaço total ocupado: {conversao_total(bytes):.2f} MB')
    relatorio.write(f'\nEspaço médio ocupado: {(total / len(dados_bytes)):.2f} MB')

with open('7-Exercicios_Arquivos/relátorio.txt', 'r') as rel:
    print(rel.read())