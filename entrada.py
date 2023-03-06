import tkinter
import tkinter as tk
from tkinter import *
import cv2




ventana: Tk = tk.Tk()
ventana.title("ASISTENCIA")
ventana.geometry("700x600+500+50")
ventana.resizable(width=False, height=False)

#boton
boton = tkinter.Button(ventana,text="INICIAR")
boton.place(x=300, y=500)

ventana.mainloop()
