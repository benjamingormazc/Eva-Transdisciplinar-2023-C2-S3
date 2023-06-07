import pandas as pd
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

def calcularVelocidad():
    metros = float(entry_desplazamiento.get())
    calcularVelocidad =  math.sqtr((2 * 9.8 * metros))

def calcularEnergiaCinetica():
    masa = float(entry_masa.get())
    velocidad = float(entry_velocidad.get())
    energia_cinetica = 0.5 * masa * velocidad**2 


    mensaje_energia_cinetica = "El valor de la energía cinética es de: {:.2f} J".format(energia_cinetica)
    label_energia_cinetica.configure(text=mensaje_energia_cinetica)

    df = pd.DataFrame({'Energía Cinética': [energia_cinetica]})

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    figura = Figure(figsize=(6, 4), dpi=80)
    eje = figura.add_subplot(111)

    df.plot(kind='bar', ax=eje, color='green', legend=False)
    eje.set_xlabel('Índice')
    eje.set_ylabel('Energía Cinética (J)')
    eje.set_title('Energía Cinética')
    eje.grid(True)

    lienzo = FigureCanvasTkAgg(figura, master=frame_grafico)
    lienzo.draw()
    lienzo.get_tk_widget().pack()

def calcular_energia_cinetica_enter(event):
    if event.keysym == 'Return':
        calcularEnergiaCinetica()

def mostrar_formula():
    ventana_formula = tk.Toplevel(window)
    ventana_formula.title("Fórmula de Energía Cinética")

    imagen = Image.open("Formula.png")
    imagen = imagen.resize((400, 300), Image.ANTIALIAS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    label_formula = tk.Label(ventana_formula, image=imagen_tk)
    label_formula.pack(padx=10, pady=10)

    ventana_formula.mainloop()
window = tk.Tk()
window.title("Cálculo de Energía Cinética")

label_desplazamiento = tk.Label(window, text="Ingresa los datos (metros de desplazamiento):")
label_desplazamiento.pack(padx=10, pady=5)

entry_desplazamiento = tk.Entry(window)
entry_desplazamiento.pack(padx=10, pady=5)
entry_desplazamiento.focus()

label_masa = tk.Label(window, text="Ingresa los datos (Masa en kg):")
label_masa.pack(padx=10, pady=5)

entry_masa = tk.Entry(window)
entry_masa.pack(padx=10, pady=5)
entry_masa.focus()

label_velocidad = tk.Label(window, text="Ingresa los datos (Velocidad en m/s):")
label_velocidad.pack(padx=10, pady=5)

entry_velocidad = tk.Entry(window)
entry_velocidad.pack(padx=10, pady=5)

button_calcular = tk.Button(window, text="Calcular", command=calcularEnergiaCinetica)
button_calcular.pack(padx=10, pady=10)

label_energia_cinetica = tk.Label(window, text="El valor de la energía cinética es de: ")
label_energia_cinetica.pack(padx=10, pady=5)

frame_grafico = tk.Frame(window)
frame_grafico.pack(padx=10, pady=10)

entry_masa.bind('<KeyPress>', calcular_energia_cinetica_enter)
entry_velocidad.bind('<KeyPress>', calcular_energia_cinetica_enter)

button_formula = tk.Button(window, text="Presiona aqui para ver la formula de energia cinetica", command=mostrar_formula)
button_formula.pack(padx=10, pady=10)

window.mainloop()
