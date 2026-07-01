###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

import re

import os
os.system("cls")

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

# text = "Hola mundo, H0la de nuevo, H$la otra vez"
# pattern = "H.la"

# found = re.findall(pattern, text)

# if found:
#     print(found)
# else:
#     print("No se ha encontrado el patron")
    
# new_text = "casa caasa cosa cisa cesa causa"
# new_pattern = "c.sa"

# matches = re.findall(new_pattern, new_text)
# print(matches)

# -------------------------------------------------------------
# Como usar la barra invertida \ para anular el significado especial de un simbolo

# text = "Mi casa es blanca. y el coche es negro."
# pattern = r"\."

# found = re.findall(pattern, text)

# if found:
#     print(found)
# else:
#     print("No se ha encontrado el patron")
    
# \d: Coincide con cualquier digito (0-9)
# text = "El numero de telefono es 3794632153"
# found = re.findall(r"\d{10}", text)
# print(found)

# Ejercicio: Detectar si hay un numero de España en el texto gracias al prefijo +34

# text = "Mi numero de telefono es +543794632153, el de mi hermana es +340303456789"
# pattern = r"\+34\d{10}"

# found = re.search(pattern, text)
# if found:
#     print(f"Encontre el numero de telefono {found.group()}")
# else:
#     print("No se ha encontrado el patron")

# \w Coincide con qualquier caracter alfanumerico (a-z, A-Z, 0-9, ...)

# text = "@@@el_rubius_69)/%$"
# pattern = r"\w"
# found = re.findall(pattern, text)
# print(found)


# \s: Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)

# text = "Hola mundo\n Como\t estas?"
# pattern = r"\s"
# found = re.findall(pattern, text)
# print(found)

# ^: Coincide con el principio de una cadena
# username = "%412_name"
# pattern = r"^\w" # Validar un nombre de usuario

# valid = re.search(pattern, username)
# if valid:
#     print("El nombre de usuario es valido")
# else:
#     print("El nombre de usuario no es valido")
    
# phone = "+543794632153"
# pattern = r"^\+\d{2}"

# valid = re.search(pattern, phone)
# if valid:
#     print("El numero es valido")
# else:
#     print("El numero no es valido")
    
# $ - Coincide con el final de una cadena
# text = "Hola mundo"
# pattern = r"mundo$"
# found = re.search(pattern, text)

# if found:
#     print("La cadena es valida")
    
# else:
#     print("La cadena no es valida")
    
# EJERCICIO
# Valida que un correo sea de GMAIl
# text = "rodrigogerometta@gmail.com"
# pattern = r"^\w+@gmail.com$"

# match = re.search(pattern, text)
# if match:
#     print("El correo es gmail")
# else:
#     print("El correo no es gmail")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
# files = "file1.txt file2.pdf midu-of.webp secret.txt"
# pattern = r"\w+\.txt"

# match = re.findall(pattern, files)
# if match:
#     print(f"Los ficheros con extension .txt son: {match}")
# else:
#     print("No hay ficheros con la extension .txt")
    
# \b: Coincide con el principio o final de una palabra
# text = "casa casada casado"
# pattern = r"\bcasa\b"

# found = re.findall(pattern, text)
# print(found)

# |: Coincide con una opcion o con otra
fruits = "platano, manzana, aguacate, palta, pera"
pattern = r"palta|aguacate"

found = re.findall(pattern, fruits)
print(found)