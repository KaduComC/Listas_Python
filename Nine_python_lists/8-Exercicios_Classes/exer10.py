# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#   tipoCombustivel.
#   valorLitro
#   quantidadeCombustivel
# Possua no mínimo esses métodos:
#   abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade 
#       de litros que foi colocada no veículo
#   abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra 
#       o valor a ser pago pelo cliente.
#   alterarValor( ) – altera o valor do litro do combustível.
#   alterarCombustivel( ) – altera o tipo do combustível.
#   alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível 
# total na bomba.

class Bomba_combustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade = quantidade

    def abastecer_valor(self, valor):
        litros_aba = valor / self.valor_litro
        return litros_aba

    def abastecer_litro(self, litros):
        valor = self.valor_litro * litros
        return valor

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        return self.valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
        return self.tipo_combustivel

    def alterar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
        return self.quantidade
        
posto = Bomba_combustivel('Gasolina', 7.85, 800)
print(posto.abastecer_valor(50))
print(posto.abastecer_litro(6))
print(posto.alterar_valor(5.50))
print()