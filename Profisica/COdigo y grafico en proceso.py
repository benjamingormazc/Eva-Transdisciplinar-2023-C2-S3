import tkinter as tk
from tkinter import ttk

def create_chart():
    data = {
        'Manzanas': 10,
        'Plátanos': 8,
        'Naranjas': 12,
        'Uvas': 5,
        'Mangos': 15
    }
    
    root = tk.Tk()
    root.title("Gráfico de Barras")

    chart_frame = ttk.Frame(root)
    chart_frame.pack(pady=10)

    for i, (label, value) in enumerate(data.items()):
        bar = ttk.Progressbar(chart_frame, length=200, maximum=max(data.values()), value=value)
        bar.grid(row=i, column=0, padx=10, pady=5)

        label = ttk.Label(chart_frame, text=f"{label}: {value}")
        label.grid(row=i, column=1, padx=10, pady=5)

    root.mainloop()

create_chart()
