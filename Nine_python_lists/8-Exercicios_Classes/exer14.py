# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario 
# (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
#   harry=funcionário("Harry",25000)
#   harry.aumentarSalario(10)

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumenta_salario(self, porcentagem):
        novo_salario = self.salario + (self.salario * (porcentagem / 100))
        return print(f'Salário com aumento: {novo_salario}')

    def mostra(self):
        return print(f'Nome: {self.nome}\nSalário: {self.salario}')

func = Funcionario('Cadu', 25000)


func.mostra()
func.aumenta_salario(10)
