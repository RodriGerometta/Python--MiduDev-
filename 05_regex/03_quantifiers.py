###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena
###

import re
import os

os.system("cls")

# *: Puede aparecer 0 o mas veces
# text = "aaaba"
# pattern = r"a*"
# matches = re.findall(pattern, text)
# print(matches)

# Ejercicio 1:
# Cuantas palabras tienen de 0 a mas "a" y despues una "b"

# text = "a aa aaa ab aab aaab ac aac aaac"
# pattern = r"a*+b"
# matches = re.findall(pattern, text)
# print(matches)

# +: Una a mas veces
# text = "dddd aaa cc aa bb a casa"
# pattern = "a+"

# match = re.findall(pattern, text)
# print(match)

# ?: Cero o una vez
# text = "aabacb"
# pattern = r"a?b"

# matches = re.findall(pattern, text)
# print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
# phone = "+34 688999999"
# pattern = r"(\+|00)?34 \d{9}"

# found = re.search(pattern, phone)
# print(found)

# {n}: Exactamente n veces
# text = "aaaaaa aa aaaa"
# pattern = "a{3}"
# matches = re.findall(pattern, text)
# print(matches)

# {n, m}: De n a m veces
# text = "u uu uuu uuuu"
# pattern = r"u{2,3}"

# matches = re.findall(pattern, text)
# print(matches)


# Ejercicio
# Encuentra las palabras de 4 a 6 letras

# words = "ala casa arbol leon cinco murcielago"
# pattern = r"\b\w{4,6}\b"

# found = re.findall(pattern, words)
# print(found)

# Ejercicio
# Encuentra las palabras de 6 letras o mas

words = "ala fantastico casa arbol leon cinco murcielago gerometta"
pattern = r"\b\w{6,}\b"

found = re.findall(pattern, words)
print(found)