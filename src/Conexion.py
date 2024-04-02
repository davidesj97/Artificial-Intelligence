import mysql.connector
from decouple import config

# establecer la conexión a la base de datos
def conexionDB():
  try:
    conexionDataBase = mysql.connector.connect(
      host=(config('host')),
      user=(config('user')),
      password=(config('password')),
      database=(config('database')),
      port=(config('port'))
    )
    return conexionDataBase
  except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))