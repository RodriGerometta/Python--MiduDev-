###
# 05 - Entrada de usuario (input()) - version simple
# La función input() se utiliza para obtener datos del usuario a través de la consola. Esta función siempre devuelve una cadena de texto (str), incluso si el usuario ingresa un número. Por lo tanto, si queremos trabajar con números, es necesario convertir la entrada a un tipo numérico utilizando funciones como int() o float().
###

# name = input("¿Cuál es tu nombre?\n")  # La función input() espera a que el usuario ingrese un valor
# print(f"Hola, {name}!")

age = input("¿Cuántos años tienes?\n")  # La entrada se almacena como una cadena de texto
age = int(age)  # Convertimos la cadena a un número entero
print(f"Tienes {age} años.")

year = int(input("¿En qué año naciste?\n"))  # Podemos combinar la conversión con la función input()
print(f"Naciste en el año {year}.")