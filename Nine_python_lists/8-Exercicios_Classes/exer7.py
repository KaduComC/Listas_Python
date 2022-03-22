# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; 
# Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em 
# consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos 
# Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar 
# esta informação por que ela pode ser calculada a qualquer momento.

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