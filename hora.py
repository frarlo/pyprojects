from tkinter import *
from time import strftime

# Inicializamos la ventana y el título de la misma:
miVentana = Tk()
miVentana.title("Reloj")

# Declaramos el objeto reloj, que mostrará la hora en la ventana:
reloj = Label(miVentana, font= ('helvetica', 30, 'bold'),
            background = 'dark blue',
            foreground = 'white')

# Declaramos y definimos la función "hora", que será utilizada por el objeto anterior para mostrar la hora:
def hora():
    # Objeto que recibe la hora
    miHora = strftime('%H:%M:%S')
    # Configuramos el reloj con la hora anterior:
    reloj.config(text = miHora)
    reloj.after(1000, hora)

# Empaquetamos todo y anclamos la hora al centro de la ventana.
reloj.pack(anchor = 'center')

# Inicializamos la lectura de la hora
hora()

# Bucle continuo de todo el programa
mainloop()
