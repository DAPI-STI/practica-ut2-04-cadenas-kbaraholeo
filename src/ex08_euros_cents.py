"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    if price_str.count(',') + price_str.count('.') != 1:
        raise ValueError("El precio debe contener exactamente una coma o un punto como separador decimal.")
    if price_str.count(',') == 1:
        c =price_str.split(',') #elimina espacios y sustituye la coma por punto
    else:
        c =price_str.split('.')
    if len(c[1]) !=2:
        raise ValueError("El precio debe tener exactamente dos decimales.")
    
    
    return  int(c[0]), int(c[1])
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    raise NotImplementedError("Implementa euros_cents(price_str)")
