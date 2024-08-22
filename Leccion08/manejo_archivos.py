try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos informacion al archivo\n')
    archivo.write('adios')
except Exception as e:
    print(e)
finally:
    print('Fin del archivo')
    archivo.close()