# Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os 
# valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção 
# secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método 
# especial str() à classe Bichinho.

from random import randrange as rd
class Bichinho_virtual:
    valor = rd(1, 11)

    def __init__(self, nome = 'Tamagushi', fome = rd(5, 21), saude = rd(5, 21), idade = 1, humor = 0):
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
        self._fome = old + 15
        if self._fome > 100:
            self._fome = 100
            print(f'\n{self._nome} foi alimentado: {old} >>> {self._fome}')
        else:
            print(f'\n{self._nome} foi alimentado: {old} >>> {self._fome}')

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

    def __str__(self):
        return f'\nNome: {self._nome}\nFome: {self._fome}\nSaude: {self._saude}\nIdade: {self._idade}\nHumor: {self._humor}'

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
    elif op == 12:
        print(b)
    else:
        print('Opção inválida')

    b.altera_idade()