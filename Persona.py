#En esta clase se crean 2 objetos personas
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Michel', 'Mulato','31')
persona1.mostrar_detalles()
#Persona.mostrar_detalles(persona1)


persona2 = Persona('Dayana', 'Droguet', '32')
persona2.mostrar_detalles()
