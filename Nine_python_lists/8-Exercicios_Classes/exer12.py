# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe 
# contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor 
# que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros 
# (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma 
# poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método 
# adicioneJuros() cinco vezes e imprime o saldo resultante.

class Conta_investimento:
    def __init__(self, numero_conta, nome, taxa_juros, saldo = 1000):
        self._numero_conta = numero_conta
        self._nome = nome
        self._saldo = saldo
        self.taxa_juros = taxa_juros

    def troca_nome(self):
        print('\n==============')
        print(f'Atual nome: {self._nome}')
        
        novo_nome = str(input('informe o novo nome: '))
        self._nome = novo_nome
        print(f'Nome alterado para: {self._nome}')

    def deposita(self):
        print('\n==============')
        valor = float(input('Valor a ser depositado: '))

        if valor > 0 and valor <= 5000:
            self._saldo += valor
            print(f'\nConta: {self._numero_conta}\nSaldo: {self._saldo:.2f}')
        else:
            print("Valos para deposito tem que ser menor ou igual a R$ 5000.00")

    def saca(self):
        print('\n==============')
        print(f'Saldo: {self._saldo:.2f}')

        valor = float(input('Valor a ser sacado: '))

        if self._saldo > 0 and self._saldo > valor:
            self._saldo -= valor
            print(f'\nConta: {self._numero_conta}\nSaldo: {self._saldo:.2f}')
        else:
            print(f"Saldo insuficiente\nSaldo: {self._saldo}")

    def mostra_saldo(self):
        print('\n==============')
        print(f'Conta: {self._numero_conta}\nSaldo: {self._saldo:.2f}')

    def add_juros(self):
        self._saldo += (self.taxa_juros / 100) * self._saldo
        print(f'Saldo com {self.taxa_juros}%: {self._saldo:.2f}')

def menu():
    numero = int(input('Número da conta: '))
    nome = str(input('Informe o nome do titular: '))
    juros = int(input('Informe a taxa de juros: '))

    ct1 = Conta_investimento(numero, nome, juros)  

    while True:
        op = int(input('\n\nMENU BANK\n==============\n'+
                '1 - Saldo\n2 - Depositar\n3 - Sacar\n4 - Trocar nome\n5 - Com juros\n6 - Sair'+
                '\nInforme a opção: '))
        
        if op == 1:
            ct1.mostra_saldo()
        elif op == 2:
            ct1.deposita()
        elif op == 3:
            ct1.saca()
        elif op == 4:
            ct1.troca_nome()
        elif op == 5:
            ct1.add_juros()
            ct1.add_juros()
            ct1.add_juros()
            ct1.add_juros()
            ct1.add_juros()
        elif op == 6:
            break
        else:
            print('opção inválida')

menu()