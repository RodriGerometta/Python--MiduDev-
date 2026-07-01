###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar diferentes bloques de código según ciertas condiciones.
###

import os
os.system("cls")  # Limpiar la consola (en Windows)

print("\nSentencias condicionales (if, elif, else)")

# edad = 18

# if edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")

# nota = int(input("Ingrese nota del alumno:"))
# if nota == 10:
#     print("Sobresaliente")
# elif (nota >= 7):
#     print("Aprobado")
# else:
#     print("Reprobado")
    
# edad = int(input("Ingrese su edad: "))
# conducira = input("Vas a conducir? (s/n): ")

# if (edad >= 18) and (conducira.lower() == "n"):
#     print("Puedes beber.")
# elif (edad >= 18) and (conducira.lower() == "s"):
#     print("No puedes beber.")
# else:
#     print("No puedes beber, eres menor de edad.")

# if edad >= 18 or conducira.lower() == "n":
#     print("Puedes beber.")
# else:
#     print("No puedes beber.") 

numero = 5

if numero: #True
    print ("El numero no es cero, El número es considerado verdadero en un contexto booleano.")
    
    
print("\nLa condicion ternaria:")
# La condición ternaria es una forma concisa de escribir una declaración if-else en una sola línea.
# La sintaxis es: valor_si_verdadero if condicion else valor_si_falso
edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)