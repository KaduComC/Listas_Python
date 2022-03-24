# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o 
# usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca 
# com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

from random import randrange as rd
class Bichinho_virtual:
    valor = 11

    def __init__(self, nome = 'Tamagushi', fome = rd(10, 31), saude = rd(10, 31), idade = 1, humor = 0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
        self._humor = humor

    def altera_nome(self):
        print(f'\nO atual nome do seu Tamagushi é: {self._nome}')

        op = str(input('Deseja alterar o nome?[S/n]\nResponda: ')).lower()

        if op == 's':
            nome_nome = str(input('Informe o novo nome: '))
            self._nome = nome_nome
        elif op == 'n':
            print('O nome não será alterado')
        else:
            print('opção inválida')

    def altera_fome(self):
        old = self._fome - self.valor
        comida = int(input('Informe a quantidade de comida: '))
        if comida > 0 and comida <= 25:
            self._fome = old + comida
            print(f'\n{self._nome} foi alimentado: {old} >>> {self._fome}')
        else:
            print('Quantidade de comida deve ser entre 1 e 25')

    def humor(self):
        self._humor = self._fome * self._saude
        print(f'Humor: {self._humor}')
    
    def altera_saude(self):
        old = self._saude - self.valor
        self._saude = old + 5
        if self._saude > 100:
            self._saude = 100
            print(f'\n{self._nome} foi medicado: {old} >>> {self._saude}')
        else:
            print(f'\n{self._nome} foi medicado: {old} >>> {self._saude}')

    def altera_idade(self):
        self._idade += 1

b = Bichinho_virtual()

while True:
    op = int(input('\n>>> TAMAGUSHI <<<'+
        '\n=================='+
        '\n1 - Alterar nome'+
        '\n2 - Dar comida'+
        '\n3 - Dar medicamento'+
        '\n4 - Humor'+
        '\n5 - Sair\nResponda: '))

    if op == 1:
        b.altera_nome()
    elif op == 2:
        b.altera_fome()
    elif op == 3: 
        b.altera_saude()
    elif op == 4:
        b.humor()
    elif op == 5:
        break
    else:
        print('Opção inválida')

    b.altera_idade()