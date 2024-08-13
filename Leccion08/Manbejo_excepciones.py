from NumerosIdenticosException import NumerosIdenticosException


resultado = None

try:

    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'ocurrio un error: {e}, {type(e)}')
else:
    print(f'No se arrojo ninguna excepcion')

finally:
    print('ejecucion de bloque finally...')

print(f'resultado: {resultado}')
print('Continuamos')
