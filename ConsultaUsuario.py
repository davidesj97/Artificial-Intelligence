import mysql.connector


def usuarios():
    conexionDataBase = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='facial_recognition',
        port='3307',
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
