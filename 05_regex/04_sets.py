import re

import os
os.system("cls")

# []: Coincide con cualquier caracter dentro de los corchetes

# username = "rub.$ius_69+"
# pattern = r"^[\w._%+-]+$"

# matches = re.search(pattern, username)
# if matches: 
#     print("El nombre de usuario es valido:", matches.group())
# else:
#     print("El nombre de usuario no es valido")

# Buscar todas las vocales de una palabra
# text = "Hola mundo"
# pattern = r"[aeiou]"

# matches = re.findall(pattern, text)
# print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
# text = "man ran fan ñan ban"
# pattern = r"[mfb]an"

# matches = re.findall(pattern, text)
# print(matches)

# Ejercicio
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban

text = "manteca fantastico baneado omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"

matches = re.findall(pattern, text)
print(matches)

# [^]: Coincide con cualquier caracter que no este dentro de los corchetes
# text = "Hola mundo"
# pattern = r"[^aeiou]"
# matches = re.findall(pattern, text)
# print(matches)