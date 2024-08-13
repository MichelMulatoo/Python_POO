from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo


#No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()


print('Creacion objeto cuadrado'.center(50, '-') )
cuadrado1 = Cuadrado(5,'rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Calculo Area cuadrado:{cuadrado1.calcular_area()}')

#MRO- Method Resolution Order
#print(Cuadrado.mro())
print(cuadrado1)
print('Creacion objeto rectangulo'.center(50, '-') )
rectangulo1 = Rectangulo(3, 8 ,'Verde')
rectangulo1.ancho = 15

print(f'Calculo area Rectangulo: {rectangulo1.calcularArea()}')
print(rectangulo1)

#Method Resolution Order
print(Cuadrado.mro())
