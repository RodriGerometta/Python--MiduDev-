###
# EJERCICIOS
###

import os

os.system("cls")  # Limpiar la consola (en Windows)

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# print("\nEjercicio 1: Determinar el mayor de dos números\n")
# num1 = float(input("Introduce el primer numero: "))
# num2 = float(input("Introduce el segundo numero: "))

# if (num1 > num2):
#     print(f"El numero {num1} es mayor que {num2}.")
# elif (num1 < num2):
#     print(f"El numero {num1} es menor que {num2}.")
# else:
#     print(f"Los numeros ingresados son iguales.")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# print("\nEjercicio 2: Calculadora simple\n")
# num1 = float(input("Introduce el primer numero: "))
# num2 = float(input("Introduce el segundo numero: "))
# operacion = input("Que operaccion deseas realizar? (+, -, *, /): ")
# if (operacion == "+"):
#     resultado = num1 + num2
#     print(f"El resultado de la suma entre {num1} y {num2} es: {resultado}")
# elif (operacion == "-"):
#     resultado = num1 - num1
#     print(f"El resultado de la resta entre {num1} y {num2} es: {resultado}")
# elif (operacion == "*"):
#     resultado = num1 * num2
#     print(f"El resultado de la multiplicacion entre {num1} y {num2} es: {resultado}")
# elif (operacion == "/"):
#     if (num1 and num2 != 0):
#         resultado = num1 / num2
#         print(f"El resultado de la division entre {num1} y {num2} es: {resultado}")
#     else:
#         print("Error: No se puede dividir entre cero.")
# else:
#     print("Operacion no valida. Por favor, elige entre +, -, *, /.")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# print("\nEjercicio 3: Año bisiesto\n")
# year = int(input("Introduce un año: "))
# if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
#     print (f"El año {year} es bisiesto.")
# else:
#     print (f"El año {year} no es bisiesto.")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# print("\nEjercicio 4: Categorizar edades\n")
# edad = int(input("Introduce una edad: "))

# if edad >= 0 and edad <= 2:
#     print(f"Con {edad} años, eres un bebe.")
# elif edad >= 3 and edad <= 12:
#     print(f"Con {edad} años, eres un niño.")
# elif edad >= 13 and edad <= 17:
#     print(f"Con {edad} años, eres un adolescente.")
# elif edad >= 18 and edad <= 64:
#     print(f"Con {edad} años, eres un adulto.")
# elif edad >= 65:
#     print(f"Con {edad} años, eres un adulto mayor.")
# else:
#     print("Edad no valida. Por favor, introduce una edad positiva.")
