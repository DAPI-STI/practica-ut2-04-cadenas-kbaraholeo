"""
Ejercicio 7: dado un correo electrónico, cambiar su dominio por "ceu.es".

La función:

Mantiene la parte local (antes de la arroba).

Sustituye el dominio por el indicado (por defecto "ceu.es").

Si el correo no tiene exactamente una arroba, lanza ValueError.
"""

def replace_domain(email: str, new_domain: str = "ceu.es") -> str:
    """Devuelve el correo con el dominio sustituido por new_domain."""
    if email.count('@') != 1:
        raise ValueError("El correo debe contener exactamente una arroba (@).")
    c=email.split('@')  #elimina espacios y separa en partes por la arroba del correo
    
    return c[0] + '@' + new_domain
    #parts[0].append('ceu.es')
    # TODO: separa con split("@"), valida y construye la nueva dirección
    raise NotImplementedError("Implementa replace_domain(email, new_domain)")
print(replace_domain("kbaraholeo@educacion.navarra.es"))  # "user@ceu.es"  