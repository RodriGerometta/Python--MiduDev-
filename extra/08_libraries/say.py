import os
import cowsay
import sys

os.system("cls")  # Limpiar la consola (en Windows)

if len(sys.argv) < 2:
    sys.exit("Too few arguments") 
elif len(sys.argv) > 2:
    sys.exit("Too many arguments") 
else:
    cowsay.cow("Hello, my name is " + sys.argv[1])  # Si el número de argumentos es correcto (exactamente uno), el programa imprimirá el mensaje de saludo con el nombre proporcionado por el usuario.