class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return  f'{self.nombre} - {otro.nombre}'

    def __sub__(self, otro):
        return self.edad - otro.edad


persona1 = Persona('Michel', 28)
persona2 = Persona('John', 20)

print(persona1 + persona2)
print(persona1 - persona2)



# obj1 + obj2
# obj1.__add__(obj2)