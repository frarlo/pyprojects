from tkinter import *
import random

# Inicializamos la ventana y el título de la misma:
miVentana = Tk()
miVentana.title("Generador de contraseñas")

# Declaramos el objeto password, que mostrará la contraseña en la ventana:
password = Label(miVentana, font= ('helvetica', 20, 'bold'),
            background = 'white',
            foreground = 'black')

# Declaramos y definimos la función "genera", que será utilizada por el objeto anterior para mostrar la contraeña
def genera():
    # Inicializamos cada variable cargada con una lista:
    lower = 'qwertyuiopasdfghjklñzxcvbnm'
    upper = 'QWERTYUIOPASDFGHJKLÑZXCVBNM'
    nums = '0123456789'
    symbs = '[]{}()*;/,._-#@'

    # Generamos una lista conjunta
    all = lower + upper + nums + symbs
    # Declaramos la longitud de la contraseña
    length = 16
    # Creamos la contraseña:
    passwordgen = "".join(random.sample(all,length))
    # Mostramos la contraseña por pantalla:
    password.config(text = passwordgen)
   

# Empaquetamos todo y anclamos la contraseña al centro de la ventana.
password.pack(anchor = 'center')

# Inicializamos el generador:
genera()

# Bucle continuo de todo el programa
mainloop()
