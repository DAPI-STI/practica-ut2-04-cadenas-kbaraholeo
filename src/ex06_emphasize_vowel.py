"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.
La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(frase: str, vocal: str) -> str:
    """
    Convierte a mayúscula todas las apariciones de vowel en la frase.
    Sugerencia:
    - Comprueba que vowel es un solo carácter y está en "aeiou" (en minúscula).
    - Recorre la frase carácter a carácter y construye una nueva cadena.
    """
    if len(vocal) !=1 or vocal.lower() not in "aeiou": #len vowel me recorre la longitud de la vocal pedida y me dice si es o no >1 vowel.lowwer() me pasa la vocal a minúscula para compararla con "aeiou"
        raise ValueError("La vocal debe ser una sola letra entre a, e, i, o, u.")
    r=''  #cadena  vacía para ir construyendo el resultado
    for char in frase:  #recorre cada carácter de la frase
        if char.lower() == vocal.lower():  #compara en minúscula
            r += char.upper()  #si coincide, añade la versión en mayúscula
        else:
            r += char  #si no coincide, añade el carácter original
    return r  #devuelve la cadena resultante    
print(emphasize_vowel("anita lava la tina","a"))  # "hOla mundO"