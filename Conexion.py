import mysql.connector
# establecer la conexión a la base de datos
def conexionDB():
  try:
    conexionDataBase = mysql.connector.connect(
      host='sql9.freemysqlhosting.net',
      user='sql9620308',
      password='RDZL4Z4vQv',
      database='sql9620308',
      port='3306'
    )
    return conexionDataBase
  except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))