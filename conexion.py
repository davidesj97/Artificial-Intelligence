import mysql.connector
import cv2

# Definimos los permisos para acceder a la base de datos
mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

# Creamos la tabla donde se almacenarán los rostros
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE rostros (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), imagen MEDIUMBLOB)")

def registrar_alumno(nombre, imagen):
    # Codifica la imagen en un array
    _, encoded_img = cv2.imencode('.jpg', imagen)
    content = encoded_img.tobytes()

    # Prepara la consulta para insertar los datos en la tabla
    sql = "INSERT INTO rostros (nombre, imagen) VALUES (%s, %s)"
    val = (nombre, content)

    # Ejecuta la consulta
    mycursor.execute(sql, val)

    # Guarda los cambios en la base de datos
    mydb.commit()

# Definimos la ruta de una imagen .jpg
imagen = cv2.imread("")

# Registra el rostro en la base de datos
registrar_alumno("", imagen)
