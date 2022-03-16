# Jogo de Craps. Faça um programa de implemente um jogo de Craps. 
# O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random as r 

print('Regras:')
print('Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou')
print('Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu')
print('Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto"')
print('- Seu objetivo agora é continuar jogando os dados até tirar este número novamente.')
print('- Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente')

print('\n\nJogar dados')

def dados():
    dado_um = r.randrange(1, 7)
    dado_dois = r.randrange(1, 7)
    return dado_um + dado_dois

valor = dados()
print('1º jogada')
if valor == 7 or valor == 11:
    print('Você ganhou na primeira rodada')
elif valor == 2 or valor == 3 or valor == 12:
    print('Você perdeu na primeira rodada')
elif valor == 4 or valor == 5 or valor == 6 or valor == 8 or valor == 9 or valor == 10:
    ponto = valor

    print(f'Seu ponto é: {ponto}')
    print('Seu objetivo agora é continuar jogando os dados até tirar este número novamente.\n')
    
    v = False
    jogada = 2
    while v == False:
        n = dados()
        print(f'\n{jogada}º jogada')
        if n == ponto:
            print(f'Você ganhou {n} = {ponto}')
            break
        elif n == 7:
            print('Voce tirou um 7 antes de repetir seu ponto, voce perdeu')
            break
        else:
            print('Ainda não acertou, nova jogada') 
        jogada += 1
