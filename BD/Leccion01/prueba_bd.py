# import psycopg2

# conexion = psycopg2.conexion(
#     user='postgres',
#     password='admin',
#     host='127.0.0.1',
#     port='5432',
#     dbname='postgres',
# )
 
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
#             entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
#             llaves_primarias = tuple(map(int, entrada.split(",")))
#             cursor.execute(sentencia, (llaves_primarias,))
#             registros = cursor.fetchall()
#             for registro in registros:
#                 print(registro)
 
# except Exception as e:
#     print(f"Ocurrio un error: {e}")
# finally:
#     conexion.close()

import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Ingresa el id_persona a eliminar (Separados por coma): ')
            valores = (tuple(entrada.split(',')),)
            cursor. execute(sentencia, valores)
            #conexion.commit()
            regitros_eliminados = cursor.rowcount
            print(f'Registro eliminado: ¨{regitros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
#             entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
#             llaves_primarias = tuple(map(int, entrada.split(",")))
#             cursor.execute(sentencia, (llaves_primarias,))
#             registros = cursor.fetchall()
#             for registro in registros:
#                 print(registros)

#Metodo para actualizar varios registros
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
#             valores =(
#                       ('Juan', 'Perez', 'jcperez@gmail.com', 1),
#                      ('Ivonnean ', 'Gutierrez', 'igutierrez@gmail.com', 2)
#             )
#             cursor. executemany(sentencia, valores)
#             #conexion.commit()
#             registros_Actualizados = cursor.rowcount
#             print(f'Registros Actualizado: ¨{registros_Actualizados}')
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
    
# finally:
#     conexion.close
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
#             valores = (
#                 ('Marcos', 'Cantu', 'mcantu@gmail.com'),
#                 ('Angel', 'Quintrana', 'aquintana@gmail.com'),
#                 ('Maria', 'Gonzalez', 'mgonzalez@gmail.com'),
#             )
#             cursor. executemany(sentencia, valores)
#             #conexion.commit()
#             registros_insertados = cursor.rowcount
#             print(f'Registros Insertados: ¨{registros_insertados}')
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
    
# finally:
#     conexion.close