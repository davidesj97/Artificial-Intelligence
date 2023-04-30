import mysql.connector

try:
    # Conectarse a la base de datos
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='facial_recognition',
        port='3307'
    )
    # Mostrar mensaje de conexión exitosa
    print("Conexión exitosa a la base de datos")

except mysql.connector.Error as error:
    # Mostrar mensaje de error si falla la conexión
    print("Error de conexión a la base de datos: {}".format(error))

'''import mysql.connector
import Inicio

def ConexionBD():
    try:
        # Conectarse a la base de datos
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='reconocimiento facial'
        )

        # Mostrar mensaje de conexión exitosa
        print("Conexión exitosa a la base de datos")
        # Ejecutar pantalla principal
        Inicio.pantalla_principal()



    except mysql.connector.Error as error:
        # Mostrar mensaje de error si falla la conexión
        print("Error de conexión a la base de datos: {}".format(error))'''