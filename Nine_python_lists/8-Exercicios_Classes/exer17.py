# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle 
# deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis 
# que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. 
# Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos 
# (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). 
# Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de 
# fome e tédio.

from random import randrange as rd
class Fazenda:
    def __init__(self, bichinho, fome = rd(0, 100), tedio = rd(0, 100)):
        self._bichinho = bichinho
        self._fome = fome
        self._tedio = tedio

    def alimentar(self):
        self._fome += 10
        print(f'\n{self._bichinho} alimentado com sucesso -> +10 food')
        if self._fome > 100:
            self._fome = 100
        else:
            self._fome = self._fome

    def brincar(self):
        self._tedio += 15
        if self._tedio < 50:
            print(f'\n{self._bichinho} ainda está com tédio')
        elif self._tedio > 100:
            self._tedio = 100
            print(f'\n{self._bichinho} não está mais com tédio')
        else:
            print(f'\n{self._bichinho} não está mais com tédio')

    def status(self):
        print(f'\nNome: {self._bichinho}\nComida: {self._fome}\nHumor: {self._tedio}')

animais = []

an1 = Fazenda('Vaca')
an2 = Fazenda('Ovelha')
an3 = Fazenda('Cavalo')

animais.append(an1)
animais.append(an2)
animais.append(an3)

while True:
    op = int(input('\nFAZENDA\n==================='+
            '\n1 - Alimentar animais\n2 - Brincar com os animais\n3 - Status dos animais\n4 - Sair'+
            '\nResponda: '))

    if op == 1:
        for i in range(len(animais)):
            animais[i].alimentar()
    elif op == 2:
        for i in range(len(animais)):
            animais[i].brincar()
    elif op == 3:
        for i in range(len(animais)):
            animais[i].status()
    elif op == 4:
        break
    else:
        print('\nOpção inválida')