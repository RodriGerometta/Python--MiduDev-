###
# 01 - Bucles (While)
# Premiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion
###

import os

os.system("cls")

# print("Ejemplo de bucle while")
# # Bucle con na simple condicion
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1 # Incrementamos el contador para evitar un bucle infinito

# # Bucle con una condicion de parada y una condicion de salida
# while True:
#     numero = int(input("Introduce un número (0 para salir): "))
#     if numero == 0:
#         print("Saliendo del bucle...")
#         break # Salimos del bucle si el numero es 0
#     else:
#         print(f"Has introducido el número: {numero}")

# # Utilizando la palabra BREAK para romper el bucle
# print("Ejemplo de bucle while con break")
# contador = 0

# while True:
#     print(contador)
#     contador += 1
#     if contador == 5:
#         break # Rompemos el bucle cuando el contador llegue a 5


## Utilizando la palabra CONTINUE para saltar a la siguiente iteracion
# print("Ejemplo de bucle while con continue")
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue # Saltamos a la siguiente iteracion si el contador es par
#     print(contador) # Solo se imprimiran los numeros impares

# # else en bucles while
# print("Ejemplo de bucle while con else")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
# else:
#     print("El bucle ha terminado")

# pedimos al usiaruio un numero que tiene que ser positivo si no, no le dejamos en paz
# numero = -1
# while numero <= 0:
#     numero = int(input("Introduce un número positivo: "))
#     if numero <= 0:
#         print("¡Eso no es un número positivo! Inténtalo de nuevo.")

# print(f"¡Gracias! Has introducido el número positivo: {numero}")

# try except para manejar errores en la entrada del usuario
numero = -1
while numero <= 0:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero <= 0:
            print("¡Eso no es un número positivo! Inténtalo de nuevo.")
    except ValueError:
        print("¡Eso no es un número válido! Inténtalo de nuevo.")

print(f"¡Gracias! Has introducido el número positivo: {numero}")
