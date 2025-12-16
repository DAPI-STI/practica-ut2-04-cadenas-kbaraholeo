"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(number: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    parts=number.strip().split("-")  #elimina espacios y separa en partes por guiones
    if not parts[0].startswith('+'): #comprueba que empieza por +, es un booleano
        raise ValueError('El número de teléfono debe comenzar con "+"') 
    if len(parts)!=3: #comprueba que hay 3 partes
        raise ValueError("El número de teléfono debe tener 3 partes separadas por guiones.")
    if not parts[1].isdigit(): #comprueba que la parte central es numérica
        raise ValueError("La parte central del número debe ser numérica.")
    return parts[1] #devuelve la parte central

    # TODO: usa .strip(), .split("-") y validaciones con .isdigit() y startswith("+")
    raise NotImplementedError("Implementa phone_core(number)")
