import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import math
import tkinter as tk
from tkinter import messagebox

# factores primos de un número
def factores_primos(n):
    i = 2
    factores = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factores.append(i)
    if n > 1:
        factores.append(n)
    return factores

#  MCD
def calcular_mcd(a, b):
    return math.gcd(a, b)

# e factores primos y su intersección
def visualizar_factores(a, b):
    factores_a = set(factores_primos(a))
    factores_b = set(factores_primos(b))
    interseccion = list(factores_a & factores_b)
    
    plt.figure(figsize=(12, 8))
    plt.title(f'Factores Primos de {a} y {b}')
    plt.text(0.3, 0.7, f'Factores de {a}: {factores_a}', ha='center', fontsize=12, bbox=dict(facecolor='blue', alpha=0.1))
    plt.text(0.7, 0.7, f'Factores de {b}: {factores_b}', ha='center', fontsize=12, bbox=dict(facecolor='orange', alpha=0.1))
    plt.text(0.5, 0.5, f'Intersección: {interseccion}', ha='center', fontsize=14, bbox=dict(facecolor='green', alpha=0.1))
    plt.axis('off')
    plt.show()

#  diagrama de Venn con  intersección
def visualizar_venn(a, b):
    factores_a = set(factores_primos(a))
    factores_b = set(factores_primos(b))
    plt.figure(figsize=(10,8))
    plt.text(0.3, 0.7, f'Factores de {a}: {factores_a}', ha='right', fontsize=14, bbox=dict(facecolor='blue', alpha=0.1))
    plt.text(0.7, 0.7, f'Factores de {b}: {factores_b}', ha='center', fontsize=12, bbox=dict(facecolor='orange', alpha=0.1))

    venn2([factores_a, factores_b], set_labels=(f'Factores de {a}', f'Factores de {b}'))
    plt.title(f'Diagrama de Venn de los Factores Primos de {a} y {b}')
    plt.show()

# Función para el botón de factores primos
def generar_factores():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        visualizar_factores(a, b)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, ingrese números enteros válidos.")

# Función para manejar el  botón de diagrama de Venn
def generar_venn():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        visualizar_venn(a, b)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, ingrese números enteros válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Visualización de MCD")

# Crear y colocar los widgets
tk.Label(root, text="Ingrese el valor de a:").grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Ingrese el valor de b:").grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=10)

btn_factores = tk.Button(root, text="Generar Factores Primos", command=generar_factores)
btn_factores.grid(row=2, column=0, padx=10, pady=10)

btn_venn = tk.Button(root, text="Generar Diagrama de Venn", command=generar_venn)
btn_venn.grid(row=2, column=1, padx=10, pady=10)


root.mainloop()
