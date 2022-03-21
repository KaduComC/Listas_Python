# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
# com valor default zero e os demais atributos são obrigatórios.
class Conta_corrente:
    def __init__(self, numero_conta, nome, saldo = 0):
        self._numero_conta = numero_conta
        self._nome = nome
        self._saldo = saldo

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

def menu():
    ct1 = Conta_corrente(123, 'Cadu')  

    while True:
        op = int(input('\n\nMENU BANK\n==============\n'+
                '1 - Saldo\n2 - Depositar\n3 - Sacar\n4 - Trocar nome\n5 - Sair'+
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
            break
        else:
            print('opção inválida')

menu()