# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um 
# local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés 
# necessárias para o local.
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mostra_lados(self):
        return print(f'Base: {self.base}\nAltura: {self.altura}')

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def trocar_valores(self):
        troca = str(input('Deseja trocar os valores?[S/n]\nResponda: ')).lower()

        if troca == 's':
            nova_base = int(input('Novo valor para a base: '))
            nova_altura = int(input('Novo valor para a altura: '))
            self.base = nova_base
            self.altura = nova_altura
            self.mostra_lados()
            self.area()
            self.perimetro()
        elif troca == 'n':
            print(f'Você não mudou nenhum valor')
        else:
            print('Opção inválida')

teste = Retangulo(4, 10)

teste.mostra_lados()
print(f'Area: {teste.area()}')
print(f'perimetro: {teste.perimetro()}')

teste.trocar_valores()

base = int(input('Informe a base do local: '))
altura = int(input('Informe altura do local: '))

teste2 = Retangulo(base, altura)
a = teste2.area()
p = teste2.perimetro()

print(f'A quantidade de pisos é de {a} e de rodapés é de {p} necessárias para o local.')