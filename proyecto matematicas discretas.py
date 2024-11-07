import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Crear conjuntos de ejemplo
conjunto1 = set(['A', 'B', 'C', 'D'])
conjunto2 = set(['D', 'E', 'F'])

# Crear y mostrar el diagrama de Venn
venn2([conjunto1, conjunto2])
plt.show()
