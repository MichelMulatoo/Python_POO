
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad (Km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo


#Creamos un objeto de la clase vehiculo
vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)

#Creamos un objeto de la clase hija Coche
coche = Coche('Azul', 4, 150)
print(coche)

#Creamos un objeto de la clase hija de coche
bicicleta = Bicicleta('blanca',2 , 'urbano')
print(bicicleta)



