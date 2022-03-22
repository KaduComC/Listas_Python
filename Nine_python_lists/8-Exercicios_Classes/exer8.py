# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
# e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, 
# criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando 
# o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. 
# É possível criar um macaco canibal?
import time
class Macaco:
    def __init__(self, nome, bucho = []):
        self.nome = nome
        self.bucho = bucho

    def comer(self):
        comida = str(input('\nInforme a comida: '))
        self.bucho.append(comida)

    def ver_bucho(self):
        for i in self.bucho:
            print('Comida: ',i)

    def digerir(self):
        self.bucho.clear()
        time.sleep(5)
        print('\nBucho vazio')
    
    def opcao(self):
        while True:
            op = int(input('\n1 - Comer\n2 - Ver bucho\n3 - Digerir\n4 - Sair\nResponda: '))
        
            if op == 1:
                self.comer()
            elif op == 2:
                self.ver_bucho()
            elif op == 3:
                self.digerir()
            elif op == 4:
                break
            else:
                print('Opção inválida')

mamaco1 = Macaco('Cadu')
mamaco2 = Macaco('Kadu')

while True:
    op = int(input('\n1 - Macaco 1\n2 - Macaco 2\n3 - Sair\nEscolha: '))

    if op == 1:
        mamaco1.opcao()
    elif op == 2:
        mamaco2.opcao()
    elif op == 3:
        break
    else:
        print('Opção inválida')

    