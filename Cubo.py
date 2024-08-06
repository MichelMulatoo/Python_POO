class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo


    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo


ancho = int(input("Digite o valor do ancho:"))
alto = int(input("Digite o valor do alto:"))
profundo = int(input("Digite o valor do profundo:"))

cubo1 = Cubo(ancho, alto, profundo)
print(f'Volumen cubo: {cubo1.calcular_volumen()}')