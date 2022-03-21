# Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e 
# um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos
# para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostra_nome(self):
        return print(f'Nome: {self.nome}')
        
    def mostra_salario(self):
        return print(f'Salário: {self.salario:.2f}')

func = Funcionario('Cadu', 1000.00)

func.mostra_nome()
func.mostra_salario()