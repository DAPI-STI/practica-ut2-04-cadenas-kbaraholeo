"""
Ejercicio 10: leer una lista de productos separados por comas y mostrar cada uno en una línea.

La función:

Recibe una cadena tipo "pan, leche, huevos".

Devuelve una lista con ["pan", "leche", "huevos"], sin espacios sobrantes.
"""

def split_products(csv_line: str) -> list[str]:
    """Devuelve una lista de productos sin espacios extra a partir de una línea CSV simple."""
    productos = csv_line.split(",")
    l=[]
    for p in productos:
        if p !=" ":
            l.append(p.strip())
           # raise ValueError("Producto vacío")
        #elif p=="":
           # raise ValueError("Producto vacío")
       # else:
            #l.append(p.strip())
    return l
print(split_products("pan, leche, huevos"))
    # TODO: usa .split(",") y .strip() para limpiar espacio