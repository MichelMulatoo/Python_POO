from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creacion objeto cuadrado'.center(50, '-') )
cuadrado1 = Cuadrado(5,'rojo')

print(f'Calculo Area cuadrado:{cuadrado1.calcular_area()}')

#MRO- Method Resolution Order
#print(Cuadrado.mro())
print(cuadrado1)
print('Creacion objeto rectangulo'.center(50, '-') )
rectangulo1 = Rectangulo(3, 8 ,'Verde')
print(f'Calculo area Rectangulo: {rectangulo1.calcularArea()}')
print(rectangulo1)