###
# 04 - Functions exercises
# Ejercicios para practicar la definicion y uso de funciones.
# Toma todos los ejercicios hechos de los modulos anteriores y ahora hazlos usando funciones para organizar mejor el codigo y hacerlo reutilizable.
###

import os
os.system("cls")

# def hola_mundo():
#     print("Hola mundo!")
    
# hola_mundo()

###                ###
# 01_if_exercises.py #
###                ###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# while True:
#     try:
#         num1 = float(input("Introduce un numero: "))
#         num2 = float(input("Introduce otro numero: "))
#         break
#     except ValueError:
#         print("Error: Por favor, ingresa numeros validos.")
        
# def mayor(num1, num2):
#     if num1 > num2:
#         print(f"El numero {num1} es mayor al numero {num2}.")
#     elif num1 < num2:
#         print(f"El numero {num2} es mayor al numero {num1}.")
#     else:
#         print("Los numeros ingresados son iguales.")
                
# mayor(num1, num2)

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

def ingresos_datos():
    while True:
        try:
            num1 = float(input("Introduce un numero: "))
            num2 = float(input("Introduce otro numero: "))
            break
        except ValueError:
            print("Error: Por favor, ingresa numeros validos.")
    return num1, num2

def suma(num1, num2):
    resultado = num1 + num2
    print(f"El resultado de la suma entre {num1} y {num2} es {resultado}.")
    
def resta(num1, num2):
    resultado = num1 - num2
    print(f"El resultado de la resta entre {num1} y {num2} es {resultado}.")
    
def multiplicacion(num1, num2):
    resultado = num1 * num2
    print(f"El resultado de la multiplicacion entre {num1} y {num2} es {resultado}.")
    
def division(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la division entre {num1} y {num2} es {resultado}.")
    else:
        print("Error: No se puede dividir entre cero.")
    
def calculadora(num1, num2):
    
    while True:
        
        operacion = input("Que operacion deaseas realizar? (+, -, *, /): ").strip()
        if operacion == "+":
            suma(num1,num2)
        elif operacion == "-":
            resta(num1, num2)
        elif operacion == "*":
            multiplicacion(num1, num2)
        elif operacion == "/":  
            division(num1, num2)
        else: 
            print("Operacion no valida. Por favor, elige entre +, -, *, /.")
            continue # Si la operacion no es valida, se vuelve a pedir la operacion sin salir del programa.
        break # Si la operacion es valida, se realiza la operacion y se sale del programa.
        

# Ejecucion del programa
num1, num2 = ingresos_datos()
calculadora(num1, num2)