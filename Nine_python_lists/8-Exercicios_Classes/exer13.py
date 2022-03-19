# Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e 
# um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos
# para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostra(self):
        return print(f'Nome: {self.nome}\nSalário: {self.salario}')

func = Funcionario('Cadu', 1000.0)

func.mostra()