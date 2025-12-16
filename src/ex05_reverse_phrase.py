"""
Ejercicio 5: escribir una frase y mostrarla invertida (carácter a carácter).
"""

def reverse_phrase(s: str) -> str:
    """Devuelve la frase invertida (carácter a carácter)."""
    f=s[::-1]
    return f #º Retorna la frase invertida
    # TODO: usa slicing con paso negativo: s[::-1]
    raise NotImplementedError("Implementa reverse_phrase(s)")
