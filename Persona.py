#En esta clase se crean 2 objetos personas
class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalles(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Michel', 'Mulato','31', 2, 3, 5, m='manzana', p='pera')
persona1.mostrar_detalles()



persona2 = Persona('Dayana', 'Droguet', '32')
persona2.mostrar_detalles()
