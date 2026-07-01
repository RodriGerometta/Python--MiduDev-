###
# EJERCICIOS (while)
###

import os

os.system("cls")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")
# numero = 10
# while numero >= 1:
#     print(numero)
#     numero -= 1  # Decrementamos el número para la cuenta atrás

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")
# numero = 0
# pares = 0
# while numero <= 20:
#     if numero % 2 == 0:
#         print(numero)  # Imprime el número par
#         pares = pares + numero  # Suma el número par a la variable 'pares'
#     numero += 1  # Incrementamos el número para continuar el bucle
# print(f"La suma entre los numeros pares entre 1 y 20 es: {pares}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

while True:
    try:
        numero = int(input("Introduce un numero entero positivo para calcular su factorial: "))
        if numero < 0:
            print("Eso no es un numero entero positivo. Intentalo de nuevo.")
        else:
            break # Salimos del bucle si el número es válido
    except ValueError:
        print("Es no es un numero valido. Intentalo de nuevo.")
        
resultado = 1
numero2 = numero  # Guardamos el valor original del número para mostrarlo al final
while numero >= 1:
    resultado *= numero  # Multiplicamos el resultado por el número actual
    numero -= 1  # Decrementamos el número para continuar el bucle
print(f"El factorial de {numero2} es: {resultado}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

# contraseña = ""
# while len(contraseña) < 8:
#     contraseña = input("Introduce una contraseña (al menos 8 caracteres): ")
#     if contraseña == "":
#         print("¡La contraseña no puede estar vacía! Inténtalo de nuevo.")
#     elif len(contraseña) < 8:
#         print("¡La contraseña es demasiado corta! Inténtalo de nuevo.")
# print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")
# while True:
#     try:
#         numero = int(input("Introduce un numero para mostrar su tabla de multiplicar (del 1 al 10): "))
#         break # Salimos del bucle si el número es válido
#     except ValueError:
#         print("¡Eso no es un número válido! Inténtalo de nuevo.")

# contador = 1
# resultado = 0
# while contador <= 10:
#     resultado = numero * contador
#     print(f"{numero} x {contador} = {resultado}")
#     contador += 1  # Incrementamos el contador para continuar el bucle
    

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# print("\nEjercicio 6:")

# while True:
#     try:
#         N = int(input("Introduce un numero entero positivo para mostrar los numeros primos menores o iguales a ese numero: "))
#         if N < 0:
#             print("Ese numero no es un numero entero positivo. Intentalo de nuevo.")
#         else: 
#             break # Salimos del bucle si el número es válido
#     except ValueError:
#         print("¡Eso no es un número válido! Inténtalo de nuevo.")

# numero = 2
# while numero <= N:
#     es_primo = True #Asumimos que el número es primo hasta que se demuestre lo contrario
#     divisor = 2
#     while divisor * divisor <= numero: # Solo necesitamos verificar hasta la raíz cuadrada del número
#         if numero % divisor == 0: # Si el número es divisible por algún divisor, no es primo
#             es_primo = False
#             break # Salimos del bucle si encontramos un divisor
#         divisor += 1 # Incrementamos el divisor para verificar el siguiente número
#     if es_primo:
#         print(numero) # Imprimimos el número primo
        
#     numero += 1 # Incrementamos el número para verificar el siguiente número