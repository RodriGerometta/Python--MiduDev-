# ###
# # exercises.py
# # Ejercicios para practicar los conceptos aprendidos en las lecciones.
# ###

# from os import system
# if system("clear") != 0: system("cls")

# print("\nEjercicio 1: Imprimir mensajes")
# print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# ### Completa aquí
# name = input("What is your name?\n")
# city = input("Where do you live?\n")
# print(f"My name is {name}\nI live in {city}")
# print("--------------")

# print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
# print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
# a = 15
# print(f"Variable a: {a} - Tipo de variable: {type(a)}")
# b = 3.14159
# print(f"Variable b: {b} - Tipo de variable: {type(b)}")
# c = "Hola mundo"
# print(f"Variable c: {c} - Tipo de variable: {type(c)}")
# d = True
# print(f"Variable d: {d} - Tipo de variable: {type(d)}")
# e = None
# print(f"Variable e: {e} - Tipo de variable: {type(e)}")

# ### Completa aquí

# print("--------------")

# print("\nEjercicio 3: Casting de tipos")
# print("Convierte la cadena \"12345\" a un entero y luego a un float.")
# print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# print("--------------")
# ### Completa aquí
# cadena = "12345"
# print(f"Cadena original: '{cadena}' - Tipo: {type(cadena)}")
# entero = int(cadena)
# print(f"Cadena convertida a entero: {entero} - Tipo: {type(entero)}")
# flotante = float(entero)
# print(f"Entero convertido a float: {flotante} - Tipo: {type(flotante)}")
# numero_flotante = 3.99
# print(f"Número flotante original: {numero_flotante} - Tipo: {type(numero_flotante)}")
# entero_redondeado = int(numero_flotante)
# print(f"Número flotante convertido a entero: {entero_redondeado} - Tipo: {type(entero_redondeado)}")
# print("Al convertir el float 3.99 a un entero, se redondea hacia abajo, resultando en 3.")  
# print("--------------")

# print("\nEjercicio 4: Variables")
# print("Crea variables para tu nombre, edad y altura.")
# print("Usa f-strings para imprimir una presentación.")

# # "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

# print("--------------")
# ### Completa aquí
# name = "Rodrigo"
# age = 30
# height = 1.83
# print(f"Hi! My name is {name}, I am {age} year old and I am {height}")
# print("--------------")

# print("\nEjercicio 5: Números")
# print("1. Crea una variable con el número PI (sin asignar una variable)")
# print("2. Redondea el número con round()")
# print("3. Haz la división entera entre el número que te salió y el número 2")
# print("4. El resultado debería ser 1")

# print("--------------")
# ### Completa aquí
# pi = 3.14
# print(f"El número PI es: {pi}")
# pi_redondeado = round(pi)
# print(f"El número PI redondeado es: {pi_redondeado}")
# print(f"La division entera entre {pi_redondeado} y 2 es: {pi_redondeado//2} ")
# print("--------------")