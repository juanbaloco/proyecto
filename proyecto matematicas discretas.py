import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

def obtener_factores_primos(numero):
    """Realiza la factorización en primos y devuelve un conjunto con los factores primos únicos."""
    factores = set()
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.add(divisor)
            numero //= divisor
        divisor += 1
    return factores

def calcular_mcd(factores1, factores2):
    """Calcula el MCD a partir de los factores primos comunes de ambos números."""
    factores_comunes = factores1.intersection(factores2)
    mcd = 1
    for factor in factores_comunes:
        mcd *= factor
    return mcd

def mostrar_diagrama_venn(factores1, factores2):
    """Genera y muestra un diagrama de Venn con los factores primos de ambos números y sus elementos específicos."""
    plt.figure(figsize=(6, 6))
    
    # Crear el diagrama de Venn con los conjuntos
    venn = venn2([factores1, factores2], set_labels=('Factores de N1', 'Factores de N2'))
    
    # Configurar las etiquetas de cada sección del diagrama
    venn.get_label_by_id('10').set_text('\n'.join(map(str, factores1 - factores2)))  # Solo en N1
    venn.get_label_by_id('01').set_text('\n'.join(map(str, factores2 - factores1)))  # Solo en N2
    venn.get_label_by_id('11').set_text('\n'.join(map(str, factores1 & factores2)))  # En la intersección

    plt.title("Diagrama de Venn de los Factores Primos")
    plt.show()

def calcular():
    """Función que calcula los factores primos y el MCD, y muestra el diagrama de Venn."""
    try:
        numero1 = int(entry_numero1.get())
        numero2 = int(entry_numero2.get())
        
        # Obtener los factores primos únicos de ambos números
        factores1 = obtener_factores_primos(numero1)
        factores2 = obtener_factores_primos(numero2)
        
        # Mostrar la factorización de cada número
        label_factores1.config(text=f"Factores primos de {numero1}: {factores1}")
        label_factores2.config(text=f"Factores primos de {numero2}: {factores2}")
        
        # Calcular y mostrar el MCD
        mcd = calcular_mcd(factores1, factores2)
        label_mcd_result.config(text=f"MCD: {mcd}")
        
        # Mostrar el diagrama de Venn
        mostrar_diagrama_venn(factores1, factores2)
    
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingresa valores enteros válidos.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Factorización en Primos, Cálculo de MCD y Diagrama de Venn")
root.geometry("500x350")

# Etiquetas y campos de entrada para los dos números
tk.Label(root, text="Ingrese el primer número entero:").pack()
entry_numero1 = tk.Entry(root)
entry_numero1.pack()

tk.Label(root, text="Ingrese el segundo número entero:").pack()
entry_numero2 = tk.Entry(root)
entry_numero2.pack()

# Botón para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

# Etiquetas para mostrar los resultados de factorización y MCD
label_factores1 = tk.Label(root, text="Factores primos de primer número: ")
label_factores1.pack()

label_factores2 = tk.Label(root, text="Factores primos de segundo número: ")
label_factores2.pack()

label_mcd_result = tk.Label(root, text="MCD: ")
label_mcd_result.pack()

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
