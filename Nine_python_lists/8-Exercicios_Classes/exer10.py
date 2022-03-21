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
        self._quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, numero):
        self._quantidade = numero

    def abastecer_valor(self):
        valor = float(input('\nInforme o valor a ser abastecido: '))
        litros_aba = valor / self.valor_litro
        if litros_aba <= self._quantidade:
            self._quantidade -= litros_aba
            print(f'{litros_aba} litros abastecidos por {valor}')
        else:
            print('Bomba de combustível incapaz de abastecer')

    def abastecer_litro(self):
        litros = int(input('\nInforme a quantidade de litros a ser abastecida: '))
        if litros <= self._quantidade:
            valor = self.valor_litro * litros
            self._quantidade -= litros
            print(f'Valor a ser pago por {litros} é de: {valor:.2f}')
        else:
            print('Bomba de combustível incapaz de abastecer')

    def alterar_valor(self):
        novo_valor = float(input('\nInforme o novo valor do combustível: '))
        antigo = self.valor_litro
        self.valor_litro = novo_valor
        print(f'Preço antigo {antigo} >> >> >> >> >> Preço novo {self.valor_litro}')

    def alterar_combustivel(self):
        novo_comb = str(input('\nInforme o novo tipo de combustível disponível: '))
        antigo = self.combustive
        self.combustive = novo_comb
        print(f'Combustível antigo {antigo} >> >> >> >> >> Novo combustível {self.combustive}')

    def alterar_quantidade(self):
        nova_qt = int(input('\nInforme a nova quantidade de combustível disponível: '))
        antigo = self._quantidade
        self._quantidade = nova_qt
        print(f'Quantidade antiga {antigo} >> >> >> >> >> Nova quantidade {self._quantidade}')

    def __str__(self):
        return f'\nCombustível disponível na bomba de {self.tipo_combustivel}: {self._quantidade}'

posto = Bomba_combustivel('Gasolina', 7.85, 800)

while True:
    op = int(input('\n\nPOSTO AT\n=========================================='+
            '\n1 - Abastecer por valor\n2 - Abastecer por litro'+
            '\n3 - Alterar valor\n4 - Alterar tipo de combustível'+
            '\n5 - Alterar quantidade do combustível disponível'+
            '\n6 - Bomba disponível'+
            '\n7 - Sair'
            '\nEscolha: '))
        
    if op == 1:
        posto.abastecer_valor()
    elif op == 2:
        posto.abastecer_litro()
    elif op == 3:
        posto.alterar_valor()
    elif op == 4:
        posto.alterar_combustivel()
    elif op == 5:
        posto.alterar_quantidade()
    elif op == 6:
        print(posto)
    elif op == 7:
        break
    else:
        print('Opção inválida')