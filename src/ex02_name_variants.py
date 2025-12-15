"""
Ejercicio 2: leer un nombre completo (nombre + apellidos) y mostrar:

Todo en minúsculas.

Todo en mayúsculas.

Capitalizado (primera letra de cada palabra en mayúscula).

La función devolverá una tupla: (minusculas, mayusculas, capitalizado).
"""

def name_variants(full_name: str) -> tuple[str, str, str]:
    lista1=[]
    lista2=[]
    lista3=[]
    lista1.append(full_name.lower())
    lista2.append(full_name.upper())
    lista3.append(full_name.title())
    return (''.join(lista1), ''.join(lista2), ''.join(lista3))

    """Devuelve (minusculas, MAYUSCULAS, Capitalizado-Por-Palabra)."""
    # TODO: usa los métodos .lower(), .upper() y .title() de str
    raise NotImplementedError("Implementa name_variants(full_name)")
print(name_variants("Juan Pérez Gómez"))  # ('juan pérez gómez', 'JUAN PÉREZ GÓMEZ', 'Juan Pérez Gómez')