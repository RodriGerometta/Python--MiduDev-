###
# 04 - Variables
# Las variables son contenedores que almacenan datos. En Python, no es necesario declarar el tipo de variable, ya que es un lenguaje de tipado dinámico.
# Python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de variable. El tipo se determina automáticamente en tiempo de ejecución.
###

# Para poder asignar un valor a una variable, simplemente escribimos el nombre de la variable seguido del signo igual (=) y el valor que queremos asignar.
# my_name = "Rodrigo"
# print(my_name)

# age = 30
# print(age)

# age = 31
# print(age)

# PY es de tipado dinamico, lo que significa que el tipo de variable se determina automáticamente en tiempo de ejecución. Esto permite cambiar el tipo de una variable sin necesidad de declararla nuevamente.

# name = "Rodrigo"
# print(type(name))  # <class 'str'>

# name = 30
# print(type(name))  # <class 'int'>

# Tipado fuerte: Python es un lenguaje de tipado fuerte, lo que significa que no se pueden realizar operaciones entre tipos incompatibles sin una conversión explícita. Por ejemplo, no se puede sumar un número entero y una cadena de texto sin convertir uno de ellos a un tipo compatible.

# print(10 + "20")  # Esto generará un error

# la utilizacion de "f-strings" para formatear cadenas de texto. Las f-strings permiten incluir expresiones dentro de una cadena de texto utilizando llaves {}.

# name = "Rodrigo"
# age = 30
# print(f"My name is {name} and I am {age} years old.") 