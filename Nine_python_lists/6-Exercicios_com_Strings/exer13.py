# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar 
# uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista 
# de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador terá seis tentativas para adivinhar a palavra. 
# Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
from random import sample as sam
import random

def tentativa():
    palavra = random_word()
    print('\n', embaralhada(palavra))
    tentativa = 1
    while tentativa <= 6:
        adivinha = str(input('\nInforme a palavra: ')).lower()
        if adivinha == palavra:
            print(f'\nVocê acertou a palavra na {tentativa} tentativa')
            break
        else:
            print(f'\nVocê não acertou a palavra. {6 - tentativa} tentativas restantes')
            tentativa += 1

def random_word():
    arquivo_jogo = open('6-Exercicios_com_Strings/palavras.txt', 'r')
    words = arquivo_jogo.read()
    word = list(map(str, words.split())) #faz uma lista e colaca as palavras dentro dela usaando 
    # o map que passa str e .split como argumentos
    return random.choice(word)

def embaralhada(palavra):
    embararalha = sam(palavra, len(palavra))
    return ''.join(embararalha)

if(__name__ == "__main__"):
    tentativa()