# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class tv:
    def __init__(self, canal = 2, volume = 15):
        self._canal = canal
        self._volume = volume

    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, numero):
        if numero < 0 or numero > 300:
            print('Canal inexistente')
        else:
            self._canal = numero

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, numero):
        if numero < 0 or numero > 100:
           print('Volume inexistente')
        else:
            self._volume = numero

    def muda_canal(self):
        numero = int(input('Canal: '))
        self.canal = numero

    def muda_volume(self):
        numero = int(input('Volume: '))
        self.volume = numero

    def __str__(self):
        return f'\nCanal: {self._canal}\nVolume: {self._volume}'

tv = tv()

while True:
    print(tv)
    
    tv.muda_canal()
    tv.muda_volume()