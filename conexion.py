import cv2
import sqlite3

# Conecta a la base de datos.
conn = sqlite3.connect('facial-recognition.sql')

# Crea la tabla para almacenar los datos de las caras.
conn.execute('''CREATE TABLE IF NOT EXISTS ESTUDIANTE
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NOMBRE TEXT NOT NULL,
             CARA BLOB NOT NULL);''')

# Agrega un usuario a la base de datos.
nombre = 'David'
cara = cv2.imread('David.jpg')
conn.execute("INSERT INTO estudiantes (NOMBRE, CARA) VALUES (?, ?)",
             (nombre, sqlite3.Binary(cv2.imencode('.jpg', cara)[1])))

# Busca un usuario por su cara.
cara_busqueda = cv2.imread('busqueda.jpg')
cursor = conn.execute("SELECT NOMBRE FROM estudiantes WHERE CARA = ?",
                      (sqlite3.Binary(cv2.imencode('.jpg', cara_busqueda)[1]),))
result = cursor.fetchone()
if result is not None:
    nombre = result[0]
    print('Estudiante:', nombre)

# Guarda los cambios en la base de datos.
conn.commit()

# Cierra la conexión a la base de datos.
conn.close()
