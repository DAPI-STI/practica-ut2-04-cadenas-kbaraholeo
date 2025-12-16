from ex01_repeat_name import repeat_name
from ex02_name_variants import name_variants
from ex03_name_length import name_upper_and_length
from ex04_phone_core import phone_core
from ex05_reverse_phrase import reverse_phrase
from ex06_emphasize_vowel import emphasize_vowel
from ex07_replace_domain import replace_domain
from ex08_euros_cents import euros_cents
from ex09_parse_date import parse_date
from ex10_split_products import split_products
from ex11_format_product import format_product
print(repeat_name("Ana", 3))
print(name_variants("Juan Pérez Gómez"))
print(name_upper_and_length('Juan Perez Gomez'))  # ('JUAN PÉREZ GÓMEZ', 13)
print(phone_core("+34-913724710-56"))  # "913724710"
print(reverse_phrase("Hola mundo"))  # "odnum aloH"
print(emphasize_vowel("anita lava la tina","a"))  # "hOla mundO"
print(replace_domain("kbaraholeo@educacion.navarra.es"))  # "user@ceu.es"  
print(euros_cents("67,89"))   # (67, 89),
print(euros_cents("123.45"))  # (123, 45)
print(parse_date("01/01/2020"))  # (1, 1, 2020)
print(split_products("pan, leche, huevos"))  # ['pan', 'leche', 'huevos']
print(format_product("Manzanas", 1.5, 20))