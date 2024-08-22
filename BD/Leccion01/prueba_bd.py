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

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()