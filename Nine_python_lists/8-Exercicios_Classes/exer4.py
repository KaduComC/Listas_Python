# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que 
# nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        return self.idade + anos

    def engordar(self, mais_peso):
        return self.peso + mais_peso

    def emagrecer(self, menos_peso):
        return self.peso - menos_peso

    def crescer(self, anos):
        if self.idade < 21:
            return self.altura + (0.05 * anos)
        else:
            return self.altura

pes = Pessoa('Cadu', 21, 100, 1.81)

anos = 2
mais_peso = 5
menos_peso = 5

print(f'Nome: {pes.nome}\nIdade: {pes.envelhecer(anos)}\nAltura: {pes.crescer(anos)}\nPeso/Emagrecer: {pes.emagrecer(menos_peso)}\nPeso/Engordar: {pes.engordar(mais_peso)}')
