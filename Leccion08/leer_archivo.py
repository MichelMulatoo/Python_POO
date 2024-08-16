

#archivo = open('C:\\PythonPOO\\POO\\Leccion08\\prueba.txt', 'r', encoding='utf8')
archivo = open('prueba.txt', 'r', encoding='utf8')


#Leer algunos caracteres
#print(archivo.read())
# print(archivo.read(21))

#Leer lineas completas
# print(archivo.readline())

#Iterar el archivo
# for linea in archivo:
#     print(linea)

#Acceder a una linea de la lista
# print(archivo.readline()[3])

#abrimos una nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('sea terminado el proceso de leer y copiado de archivo')
