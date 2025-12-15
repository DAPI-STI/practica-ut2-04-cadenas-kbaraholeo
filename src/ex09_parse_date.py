"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    parts = date_str.split('/')
    if not all(part.isdigit() for part in parts):
        raise ValueError("La fecha debe contener solo números y '/'.")
    
    if len(parts) != 3:
        raise ValueError("La fecha debe tener el formato dd/mm/aaaa.")
    if len(parts[0]) !=1 and len(parts[0]) !=2:
        raise ValueError("El día debe tener uno o dos dígitos.")
    if len(parts[1]) !=1 and len(parts[1]) !=2:
        raise ValueError("El mes debe tener uno o dos dígitos.")
    if len(parts[2]) !=4:   
        raise ValueError("El año debe tener cuatro dígitos.")
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    if not (1 <= day <= 31):
        raise ValueError("El día debe estar entre 1 y 31.") 
    if not (1 <= month <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")
    return (day, month, year)

    
print(parse_date("01/01/2020"))  # (1, 1, 2020)
