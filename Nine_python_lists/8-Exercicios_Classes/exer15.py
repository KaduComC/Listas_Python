# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o 
# usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca 
# com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

from random import randrange as rd
class Bichinho_virtual:
    def __init__(self, nome = 'Tamagushi', fome = rd(50, 100), saude = rd(50, 100), idade = 1):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade

    def altera_nome(self):
        print(f'atual nome do seu Tamagushi é: {self._nome}')

        op = str(input('Deseja alterar o nome?[S/n]\nResponda: ')).lower()

        if op == 's':
            nome_nome = str(input('Informe o novo nome: '))
            self._nome = nome_nome
        elif op == 'n':
            print('O nome não será alterado')
        else:
            print('opção inválida')

    # def altera_fome(self):
    #     print(f'Fome: {self._fome}')
        
    def humor(self):
        if self._fome > 10 and self._saude > 10:
            if self._saude > 60 and self._fome > 60:
                print('Estou muito bem')
            elif self._saude < 60 and self._saude >= 40 and self._fome < 60 and self._fome >= 40:
                print('Estou ficando ruim')
            elif self._saude < 40 and self._fome < 40:
                print('Estou muito ruim')
        else:
            print(f'{self._nome} morreu')
    
    def altera_saude(self):
        pass

    def altera_idade(self):
        self._idade += 1

    def __str__(self):
        return f'{self._saude}\n{self._fome}'
    
b = Bichinho_virtual()
b.altera_nome()
b.altera_idade()
b.humor()
print(b)