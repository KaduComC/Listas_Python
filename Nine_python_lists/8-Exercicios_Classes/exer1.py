# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def mostra_cor(self):
        print(f'\nA cor da bola é: {self.cor}')

    def troca_cor(self):
        troca = str(input('\nDeseja trocar a cor?[S/n]\nResponda: ')).lower()

        if troca == 's':
            cor_nova = str(input('Informe a nova cor: '))
            self.cor = cor_nova
            print(f'A cor da bola é: {self.cor}')
        elif troca == 'n':
            print(f'Sua cor continua como: {self.cor}')
        else:
            print(f'Resposta inválida')

bola_ex = bola('Verde', 10, 'Borracha')

bola_ex.mostra_cor()
bola_ex.troca_cor()
