import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
#++++++++++++++++++++++
# Deficion de variables
#++++++++++++++++++++++
imagen_mostrada = False

#++++++++++++++++++++++++++++++++++++++++++
# Función para calcular la energía cinética
#++++++++++++++++++++++++++++++++++++++++++
def calcular_energia_cinetica():
    masa = float(entry_masa.get())  # Obtiene el valor de masa ingresado
    velocidad = float(entry_velocidad.get())  # Obtiene el valor de velocidad ingresado
    energia_cinetica = 0.5 * masa * velocidad**2  # Calcula la energía cinética
    mensaje_energia_cinetica = "= La energía cinética es de {:.2f} Joule(s)".format(energia_cinetica)
    label_energia_cinetica.configure(text=mensaje_energia_cinetica, fg="#004d99")  # Actualiza el texto y color de la etiqueta
#+++++++++++++++++++++++++++++++++++
# Función para calcular la velocidad
#+++++++++++++++++++++++++++++++++++
def calcular_velocidad():
    masa = float(entry_masa_velocidad.get())  # Obtiene el valor de masa ingresado
    energia = float(entry_energia.get())  # Obtiene el valor de energía ingresado
    velocidad = (2 * energia / masa) ** 0.5  # Calcula la velocidad
    label_velocidad_resultado.configure(text="= La velocidad es de {:.2f} m/s".format(velocidad), fg="#004d99")  # Actualiza el texto y color de la etiqueta
#+++++++++++++++++++++++++++++++++++++
# Función para convertir de km/h a m/s
#+++++++++++++++++++++++++++++++++++++
def convertir_kmph_a_ms():
    kmph = float(entry_kmph.get())  # Obtiene el valor de km/h ingresado
    ms = kmph * (1000 / 3600)  # Convierte de km/h a m/s
    label_ms.configure(text="= {} km/h equivalen a {:.2f} m/s".format(kmph, ms), fg="#004d99")  # Actualiza el texto y color de la etiqueta

#++++++++++++++++++++++++++++++++++++++++++
# Función para mostrar formula de Velocidad
#++++++++++++++++++++++++++++++++++++++++++
def abrir_imagen():
    global imagen_mostrada
    
    imagen = Image.open("F.velocidad.png")
    imagen = imagen.resize((480, 260))
    imagen_tk = ImageTk.PhotoImage(imagen)

    if not imagen_mostrada:
        label_imagen.configure(image=imagen_tk)
        label_imagen.image = imagen_tk
        imagen_mostrada = True
    else:
        label_imagen.configure(image="")
        label_imagen.image = None
        imagen_mostrada = False
#++++++++++++++++++++++++++++++++
# Función para mostrar el grafico
#++++++++++++++++++++++++++++++++
def plot_graph():
    masa_vals = np.linspace(0, 10, 100)  # Valores de masa para el gráfico
    velocidad_vals = 10 * np.sqrt(2 * 1.0 * masa_vals)  # Fórmula de energía cinética con masa constante

    # Crear el gráfico lineal
    plt.plot(velocidad_vals, masa_vals)
    plt.xlabel('Velocidad (m/s)')
    plt.ylabel('Masa (Kg)')
    plt.title('Gráfico de Energía Cinética')

    # Mostrar el gráfico
    plt.show()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Función para cerrar la ventana cuando se presiona la tecla Escape
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cerrar_ventana(event):
    if event.keysym == 'Escape':
        window.destroy()
#+++++++++++++++++++++++++++++++++
# Creación de la ventana principal
#+++++++++++++++++++++++++++++++++
window = tk.Tk()
window.title("Cálculo de Energía Cinética")
window.attributes('-fullscreen', True)  # Ejecutar en pantalla completa
window.configure(bg="#CCCCCC")  # Establece el color de fondo en gris

fondo = Image.open("fondouwu.png")
fondo = fondo.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
fondo_tk = ImageTk.PhotoImage(fondo)
#++++++++++++++++++++++++++++++++++++++++++++
# Crear un widget Label para mostrar el fondo
#++++++++++++++++++++++++++++++++++++++++++++
label_fondo = tk.Label(window, image=fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Etiqueta y campo de entrada para la masa - ENERGIA CINETICA 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_masa = tk.Label(window, text="", fg="dark blue", bg="#CCCCCC")
label_masa = tk.Label(window, text="Calcular energía cinética.", bg="#CCCCCC", font=("Arial", 12, "bold"))
label_masa.place(x= 10, y=16 )
label_masa = tk.Label(window, text="", fg="dark blue", bg="#CCCCCC")
label_masa = tk.Label(window, text="Ingrese los datos de masa.", bg="#CCCCCC")
label_masa.place(x= 10, y= 50)
label_masa = tk.Label(window, text="Kg", bg="#CCCCCC", font=("Arial", 8,"bold"))
label_masa.place(x= 110, y= 75)
entry_masa = tk.Entry(window, text="",fg="black", font=("Arial", 8,"bold"))
entry_masa.place(x = 20, y = 75, width=75)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Etiqueta y campo de entrada para la velocidad - ENERGIA CINETICA
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_velocidad = tk.Label(window, text="Ingrese los datos de velocidad.", bg="#CCCCCC")
label_velocidad.place(x=10, y=100)
label_velocidad = tk.Label(window, text="m/s", bg="#CCCCCC", font=("Arial", 8,"bold"))
label_velocidad.place(x= 110, y= 120)
entry_velocidad = tk.Entry(window, text="",fg="black", font=("Arial", 8,"bold"))
entry_velocidad.place(x=20, y=120, width=75)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Botón para calcular la energía cinética - ENERGIA CINETICA-------------------------------------------------------------------------------------------------------------
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
button_calcular = tk.Button(window, text="Calcular", command=calcular_energia_cinetica and plot_graph)
button_calcular.place(x=19, y=155)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Etiqueta para mostrar el valor de la energía cinética calculada - ENERGIA CINETICA 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_energia_cinetica = tk.Label(window, text="=", fg="dark blue", bg="#CCCCCC", font=("Arial", 8,"bold"))
label_energia_cinetica.place(x=79, y=155)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------@
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Etiqueta y campo de entrada para la masa en el cálculo de la velocidad - CALCULO
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_masa_velocidad = tk.Label(window, text="Calcular velocidad teniendo.", bg="#CCCCCC", font=("Arial", 12, "bold"))
label_masa_velocidad.place(x=10, y=200)
label_masa_velocidad = tk.Label(window, text="masa y energia.", bg="#CCCCCC", font=("Arial", 12, "bold")) 
label_masa_velocidad.place(x=10, y=230)
label_masa_velocidad_texto = tk.Label(window, text="Ingrese los datos de masa:", bg="#CCCCCC")
label_masa_velocidad_texto.place(x=10, y=264)
label_masa_velocidad_unidad = tk.Label(window, text="Kg", bg="#CCCCCC", font=("Arial", 8, "bold"))
label_masa_velocidad_unidad.place(x=110, y=289)
entry_masa_velocidad = tk.Entry(window, text="", fg="black", font=("Arial", 8, "bold"))
entry_masa_velocidad.place(x=20, y=289, width=75)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Etiqueta y campo de entrada para la energía en el cálculo de la velocidad
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_energia_texto = tk.Label(window, text="Ingrese los datos de energía:", bg="#CCCCCC")
label_energia_texto.place(x=10, y=314)
entry_energia = tk.Entry(window, text="", fg="black", font=("Arial", 8, "bold"))
entry_energia.place(x=20, y=339, width=75)
label_energia_unidad = tk.Label(window, text="Joule(s)", bg="#CCCCCC", font=("Arial", 8, "bold"))
label_energia_unidad.place(x=110, y=339)
#+++++++++++++++++++++++++++++++++
# Botón para calcular la velocidad
#+++++++++++++++++++++++++++++++++
button_calcular_velocidad = tk.Button(window, text="Calcular", command=calcular_velocidad)
button_calcular_velocidad.place(x=19, y=374)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Etiqueta para mostrar el resultado del cálculo de la velocidad
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_velocidad_resultado = tk.Label(window, text="=", fg="dark blue", bg="#CCCCCC", font=("Arial", 8, "bold"))
label_velocidad_resultado.place(x=79, y=374)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------@
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Etiqueta y campo de entrada para la conversión de km/h a m/s - CONVERSOR VELOCIDAD KM/H A M/S
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_kmph = tk.Label(window, text="Convierte km/h a m/s.", bg="#CCCCCC", font=("Arial", 12, "bold"))
label_kmph.place(x=10, y=410)
label_kmph = tk.Label(window, text="Ingrese km/h aqui :", bg="#CCCCCC")
label_kmph.place(x=10,y=450)
entry_kmph = tk.Entry(window, text="",fg="black", font=("Arial", 8,"bold"))
entry_kmph.place(x=120, y=450, width=30)
label_kmph = tk.Label(window, text="km/h.", bg="#CCCCCC", font=("Arial", 8,"bold"))
label_kmph.place(x= 159, y= 450)
#+++++++++++++++++++++++++++++++++++
# Botón para convertir de km/h a m/s
#+++++++++++++++++++++++++++++++++++
button_convertir = tk.Button(window, text="Convertir", command=convertir_kmph_a_ms)
button_convertir.place(x=19, y=485)
#++++++++++++++++++++++++++++++++++++++++++++++++++++
# Etiqueta para mostrar el resultado de la conversión
#++++++++++++++++++++++++++++++++++++++++++++++++++++
label_ms = tk.Label(window, text="=", fg="dark blue", bg="#CCCCCC", font=("Arial", 8,"bold"))
label_ms.place(x=79, y=486)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Botón para abrir la imagen - formula energia cinetica
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
label = tk.Label(window, text= "¿Necesitas ayuda?", bg="#CCCCCC", font=("Comic Sans MS", 18, "bold"))
label.place(x=60, y=530)
button_abrir_imagen = tk.Button(window, text="Ver formula de energia cinetica.", font=("Tahoma", 8), command=abrir_imagen)
button_abrir_imagen.pack()
button_abrir_imagen.place(x=79, y=600, height=50)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Widget Label para mostrar la imagen - formula energia cinetica
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_imagen = tk.Label(window, bg="#CCCCCC")
label_imagen.pack()
label_imagen.place(x=412, y=435) #resolución para FHD= x490, y510
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Ventana llamada "Problematicas a simular" para la problematica
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label = tk.Label(window, text= "Problematicas", bg="#CCCCCC", font=("Comic Sans MS", 18, "bold"))
label.place(x=1100, y=460)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Asociar la tecla Escape a la función de cierre de ventana
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
window.bind('<Escape>', cerrar_ventana)
#++++++++++++++++++++++++++++++++++++++++++
# Ejecutar el bucle principal de la ventana
#++++++++++++++++++++++++++++++++++++++++++
window.mainloop()