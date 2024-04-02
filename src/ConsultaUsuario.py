import mysql.connector
from decouple import config

def usuarios():
    conexionDataBase = mysql.connector.connect(
        host=(config('host')),
        user=(config('user')),
        password=(config('password')),
        database=(config('database')),
        port=(config('port')),
    )

    cursor = conexionDataBase.cursor()

    cursor.execute('SELECT n_control, nombre, apellidoP, apellidoM FROM usuarios')

    resultados = cursor.fetchall()

    with open('Usuarios.txt', 'w') as archivo:
        for fila in resultados:
            linea = '\t'.join(str(valor) for valor in fila) + '\n'
            archivo.write(linea)

    cursor.close()
    conexionDataBase.close()


usuarios()
