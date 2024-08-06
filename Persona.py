#En esta clase se crean 2 objetos personas
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print('llamando metodo get nombre')
        return self._nombre

    @nombre.setter#modifica el valor de atributo
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad


    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')


    def __del__(self):# Destructor de nuestro objeto
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    persona1 = Persona('Michel', 'Mulato','31')
    persona1.nombre = 'Dayana Carrasco'

    persona1.apellido = 'Carrasco'
    persona1.edad = 25
    persona1.mostrar_detalles()

    print( __name__)