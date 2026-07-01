###
# 04 - Functions
# Bloques de codigo reutilizables que realizan una tarea específica.
###

import os
os.system("cls")

"""
Definicion de una funucion

def nombre_de_la_funcion(parametro1, parametro2,...)
    # docstring
    # cuerpo de la funcion
    return valor_de_retorno
"""

# Ejemplo de una funcion para imprimir algo en consola
# def saludar():
#     print("Hola mundo!")
    
# saludar() #Llamada a la funcion para ejecutar su codigo.

# # Ejemplo de una funcion con parametros
# def saludar_a(nombre):
#     print(f"Hola {nombre}")
    
# saludar_a("Lucila") #Llamada a la funcion con un argumento para el parametro 'nombre'.

# Parametro es lo que acepta la funcion
# Argumento es lo que se le pasa a la funcion al llamarla

# Funcion con mas parametros
# def sumar(a, b):
#     suma = a + b
#     return suma #La palabra clave 'return' se usa para devolver un valor desde la funcion.

# resultado = sumar(3, 5) #Llamada a la funcion con argumentos para los parametros 'a' y 'b', y almacenamos el valor de retorno en la variable 'resultado'.
# print(resultado) #Imprime el resultado de la suma, que es 8.
# print(sumar(10, 20)) #Llamada a la funcion con otros argumentos, e imprime el resultado de la suma, que es 30.

# # Documentar las funciones con docstrings
# def restar(a, b):
#     """Resta dos numeros y devuelve el resultado."""
#     resta = a - b
#     return resta

# print(restar(10, 4)) #Llamada a la funcion restar con argumentos, e imprime el resultado de la resta, que es 6.
# print(restar.__doc__) #Imprime el docstring de la funcion restar, que describe lo que hace la funcion.
# help(restar) #Muestra la ayuda de la funcion restar, incluyendo su docstring y su firma (parametros y valor de retorno).

# Parametros por defecto
# def multiplicar (a, b=2): #El parametro 'b' tiene un valor por defecto de 2, lo que significa que si no se le pasa un argumento al llamar a la funcion, se usara el valor 2.
#     """Multiplica dos numeros y devuelve el resultado. Si no se especifica el segundo numero, se multiplicara por 2."""
#     producto = a * b
#     return producto

# print(multiplicar(2)) #Llamada a la funcion multiplicar con un argumento para 'a', y se usara el valor por defecto de 2 para 'b', e imprime el resultado de la multiplicacion, que es 4.
# print(multiplicar(2, 3)) #Llamada a la funcion multiplicar con argumentos para 'a' y 'b', e imprime el resultado de la multiplicacion, que es 6.

# # Argumentos por palabra clave
# def describir_persona(nombre, edad, sexo):
#     """Imprime una descripcion de una persona con su nombre, edad y sexo."""
#     print(f"Soy {nombre}, tengo {edad} años y soy {sexo}.")
    
# describir_persona(nombre="Rodrigo", edad=30, sexo="Hombre") #Llamada a la funcion describir_persona con argumentos por palabra clave, e imprime la descripcion de la persona.
# describir_persona(sexo="Mujer", edad=27, nombre="Lucila") #Llamada a la funcion describir_persona con argumentos por palabra clave en un orden diferente, e imprime la descripcion de la persona.

# Argmentos de lomgitud de variable (*args)
# def sumar_numeros(*args):
#     """Suma una cantidad variable de numeros y devuelve el resultado."""
#     suma = 0
#     for numero in args: #Itera sobre los argumentos pasados a la funcion, que se almacenan en una tupla llamada 'args'.
#         suma += numero #Suma cada numero al total de la suma.
#     return suma #Devuelve el resultado de la suma.

# print(sumar_numeros(1, 2, 3)) #Llamada a la funcion sumar_numeros con tres argumentos, e imprime el resultado de la suma, que es 6.
# print(sumar_numeros(10, 20, 30, 40)) #Llamada a la funcion sumar_numeros con cuatro argumentos, e imprime el resultado de la suma, que es 100.

# Argumentos de Clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    """Muestra la informacion de una persona a partir de argumentos de clave-valor."""
    for clave, valor in kwargs.items(): #Itera sobre los argumentos pasados a la funcion, que se almacenan en un diccionario llamado 'kwargs', y obtiene la clave y el valor de cada argumento.
        print(f"{clave}: {valor}") #Imprime la clave y el valor de cada argumento.
        
mostrar_informacion_de(nombre="Rodrigo", edad=30, sexo="Hombre") #Llamada a la funcion mostrar_informacion_de con argumentos de clave-valor, e imprime la informacion de la persona.
mostrar_informacion_de(nombre="Lucila", edad=27, sexo="Mujer", profesion="Programadora") #Llamada a la funcion mostrar_informacion_de con argumentos de clave-valor adicionales, e imprime la informacion de la persona.