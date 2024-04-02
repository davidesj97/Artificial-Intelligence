from PIL import Image
from io import BytesIO
from shutil import rmtree
from tkinter import messagebox
import face_recognition as fr
import cv2
import os
import errno
import Conexion

def getUsers():
    conexion = Conexion.conexionDB()

    cursor = conexion.cursor()

    cursor.execute("SELECT n_control, nombre, apellidoP, apellidoM, rostro FROM usuarios")

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados

def searcheFace(face):
  users = getUsers()
  resultado = False
  # Crear el directorio donde se guardaran temporalmente las imagenes 
  os.makedirs('temp/img', exist_ok=True)
  i = 1
  for user in users:
    n_control, nombre, apellidoP, apellidoM, rostro = user


    # Convetir la imagen de binarios a pixeles
    image_pillow = Image.open(BytesIO(rostro))
    image_pillow.save(f"./temp/img/Usuario_{i}.jpg")

    face_load = fr.load_image_file(f"./temp/img/Usuario_{i}.jpg")

    face_load = cv2.cvtColor(face_load, cv2.COLOR_BGR2RGB)

    face_location = fr.face_locations(face_load)

    if(len(face_location) == 1):
        face_encoding = fr.face_encodings(face_load, face_location)[0]
        resultado = fr.compare_faces([face_encoding], face)

    i += 1
    if resultado:
      return {
         "n_control": n_control,
         "nombre": nombre,
         "apellidoP": apellidoP,
         "apellidoM": apellidoM
      }

  rmtree("./temp/img")
  return resultado

# Función para realizar el registro de la asistencia en la base de datos.
def register(face):
  register = searcheFace(face)
  n_control = int(register["n_control"])
  nombre = register["nombre"]
  apellidoP = register["apellidoP"]
  apellidoM = register["apellidoM"]
  if(register):
    conexion = Conexion.conexionDB()
    try:
      cursor = conexion.cursor()

      sentencia = "INSERT INTO asistencias (n_control, nombre, apellidoP, apellidoM) VALUES (%s, %s, %s, %s)"

      cursor.execute(sentencia, (n_control, nombre, apellidoP, apellidoM,))

      conexion.commit()

      conexion.close()
      messagebox.showinfo("Registro exitoso", "El registro se completó con éxito:" + str(n_control) + ", " + nombre + " " + apellidoP + " " + apellidoM)
    except Exception as error:
      print("Error inesperado: {}".format(error))
    finally:
      if conexion.is_connected():
        conexion.rollback()
        conexion.close()
        print("Conexión a la base de datos cerrada.")
  else: 
     messagebox.showerror("Error de registro", "Usuario no registrado en base de datos.")
