import mysql.connector
# establecer la conexión a la base de datos
def conexionDB():
  try:
    conexionDataBase = mysql.connector.connect(
      host='localhost',
      user='root',
      password='12345',
      database='facial_recognition',
      port='3306'
    )
    return conexionDataBase
  except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))