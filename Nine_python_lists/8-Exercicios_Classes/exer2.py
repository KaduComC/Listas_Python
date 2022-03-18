# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mostra_lado(self):
        print(f'Lado: {self.lado}')

    def muda_lado(self):
        troca = str(input('Deseja trocar o valor dos lados?[S/n]\nResponda: ')).lower()

        if troca == 's':
            novo_lado = int(input('Informe o novo valor dos lados: '))
            self.lado = novo_lado
            print(f'O novo valor dos lados é: {self.lado}')
            self.area()
        elif troca == 'n':
            print(f'O valor continua {self.lado}')
            self.area()
        else:
            print('Opção inválida')

    def area(self):
        area = self.lado ** 2
        print(f'Area: {area}')

qd = Quadrado(5)

qd.mostra_lado()
qd.area()
qd.muda_lado()