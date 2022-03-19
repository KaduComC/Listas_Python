# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
# com valor default zero e os demais atributos são obrigatórios.
class Conta_corrente:
    def __init__(self, numero_conta, nome, saldo = 0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposita(self, valor_dep):
        if self.saldo == 0: 
            self.saldo = valor_dep
            return self.saldo
        else: 
            self.saldo ++ valor_dep
            return self.saldo
        
    def saca(self, valor_sac):
        if self.saldo <= 0:
            ValueError("Saldo zerado")
        else:
            self.saldo -= valor_sac
            return self.saldo
    
cc = Conta_corrente(1, 'Kadu')

print(cc.alterar_nome('Cadu'))
print(cc.deposita(800))
print(cc.saca(500))