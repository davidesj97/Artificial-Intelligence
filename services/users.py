import face_recognition as fr
import cv2
import dlib
from PIL import Image
from io import BytesIO
import os
from shutil import rmtree

def getFaces(conexion):
  cursor = conexion.cursor()
  cursor.execute("SELECT rostro FROM usuarios")
  rostros = cursor.fetchall()
  return rostros
  # for rostro in rostros:
  #     cv2.imshow("image", rostro)
  #     cv2.waitKey(0)

# verificar si el número de control ya está registrado en la base de datos
def getUsers(n_control, conexion):
  cursor = conexion.cursor()
  consulta_sql = "SELECT * FROM usuarios WHERE n_control = %s"
  cursor.execute(consulta_sql, (n_control,))
  resultados = cursor.fetchall()
  return resultados

def compararRostros(rostroCapturado, listaRostros):
  os.makedirs('temp/img', exist_ok=True)
  resultado = False
  i = 1
  for rostro in listaRostros:

    # Convetir la imagen de binarios a pixeles
    image_pillow = Image.open(BytesIO(rostro[0]))
    image_pillow.save(f"./temp/img/Usuario_{i}.jpg")

    # Cargar imagenes
    foto_cargar = fr.load_image_file(rostroCapturado)
    foto_comparadora = fr.load_image_file(f"./temp/img/Usuario_{i}.jpg")

    # Convertir imagenes a rgb
    foto_cargar = cv2.cvtColor(foto_cargar, cv2.COLOR_BGR2RGB)
    foto_comparadora = cv2.cvtColor(foto_comparadora, cv2.COLOR_BGR2RGB)

    # Localizar cara control
    lugar_cara_foto_cargar = fr.face_locations(foto_cargar)[0]
    lugar_cara_foto_comparadora = fr.face_locations(foto_comparadora)[0]

    cara_codificada_foto_cargar = fr.face_encodings(foto_cargar)[0]
    cara_codificada_foto_comparadora = fr.face_encodings(foto_comparadora)[0]

    # Realizar comparacion
    resultado = fr.compare_faces([cara_codificada_foto_comparadora], cara_codificada_foto_cargar)

    if(resultado):
      return resultado

    i += 1

  rmtree("./temp/img")
  return resultado