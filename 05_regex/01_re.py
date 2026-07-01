###
# 01 - Expresiones regulares
#

# Las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda. Se utilizan para la busqueda de canadenas de texto, validacion de datos, etc.

# Por que aprender Regex?
# Busqueda avanzada: Encontrar patrones especificos en textos grandes de forma rapidas y precisas. (un editor de Markdown solo usando Regex).
# Validacion de datos: Asegurarte que los datos que ongresa un usuario como el email, telefono, etc, son correctos.
# Manipulacion del texto: Extraer, reemplazar y modificar partes de la cadena de texto facilmente

# Para poder trabajar con expresiones regulares tenemos que importar el modulo re

# 1. Importarr el modulo de expresiones regulares "re"
import re
import os

os.system("cls")

# 2. Crear un patron, que es una cadena de texto que describe lo que queremos encontrar
#pattern = "Hola"

# 3. El texto donde queremos buscar
#text = "Hola mundo"

# 4. Usar la  funcion de busqueda de "re"

# result = re.search(pattern, text)

# if result:
#     print("He encontrado el patron en el texto")
# else:
#     print("No he encontrado el patron en el texto")
    
# .group() Devuelve la cadena que ha encontrado con el pattern
#print(result.group())

# .start() que devuelve la posicion donde empieza la coincidencia
#print(result.start())

# .end() que devuelve la posicion donde termina la coincidencia
#print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
# text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
# pattern = "IA"
# result = re.search(pattern, text)

# if result:
#     print(f"He encontrado el patron en el texto en la posicion {result.start()} y termina en la posicion {result.end()}")
    
#     print(f"La cadena encontrada fue: {result.group()}")
# else:
#     print("No he encontrado el patron '{pattern}' en el texto")
    
# En el ejercicio anterior solo habia un patron "IA" pero que pasa cuando hay mas de uno y se quiere encontrar todos?
# .findall() devuelve una listat con todas las coincidencias

# text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python"

# pattern = "Python"

# matches = re.findall(pattern, text)

# print(matches)
# print(f"Se encontraron {len(matches)} coincidencias: {matches}")

# iter() devuelve un iterador que contiene todos los resultados de la busqueda

# text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python"

# pattern = "Python"

# matches = re.finditer(pattern, text)

# print(matches)

# for match in matches:
#     print(match.group(), match.start(), match.end())

# Modificadores
# Los modificadores son opciones que se pueden agregar a un patron para cambiar su comportamiento
# re.IGNORECASE: ignora las mayusculas y minusculas
# sencibilidad IA, Ia, iA, ia

# text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala, solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado. Viva la Ia"
# pattern = "IA"
# result = re.findall(pattern, text, re.IGNORECASE)

# if result:  
#     print(f"La cadena encontrada fue: {result}")
# else:
#     print("No he encontrado el patron '{pattern}' en el texto")
    
# Ejercicio 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayusculas y minusculas.
text = "Este es un curso de Python de midudev. suscribete a python si te gusta este contenido! PYTHON"

pattern = "python"

result = re.findall(pattern, text, re.IGNORECASE)

if result:
    print(f"La cadena encontrada fue: {result}")
else:
    print("No he encontrado el patron '{pattern}' en el texto")
    
### REEMPLAZAR EL TEXTO
# .sub() reemplaza todas las coincidencias de un patron en un texto.

replacement = "JavaScript"
new_text = re.sub(pattern, replacement, text, re.IGNORECASE)
print(new_text)