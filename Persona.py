#En esta clase se crean 2 objetos personas
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
persona1 = Persona('Michel', 'Mulato','31')
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')


persona2 = Persona('Dayana', 'Droguet', '32')
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

