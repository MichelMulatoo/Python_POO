class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calula_area(self):
        return self.base * self.altura


base = int(input('Ingresa la base: '))
altura = int(input('Ingresa la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Area de la rectangulo: {rectangulo1.calula_area()}')


base = int(input('Ingresa la base: '))
altura = int(input('Ingresa la altura: '))

rectangulo2 = Rectangulo(base, altura)
print(f'Area de la rectangulo: {rectangulo2.calula_area()}')

print()