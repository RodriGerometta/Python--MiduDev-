import sys

from ejemplo_crear_libreria import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])  # Si el número de argumentos es correcto (exactamente uno), el programa llamará a la función "goodbye" importada desde "ejemplo_crear_libreria.py" y le pasará el argumento proporcionado por el usuario.