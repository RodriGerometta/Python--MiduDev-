import sys
import os

os.system("cls")  # Limpiar la consola (en Windows)

 
# print("Hello, my name is", sys.argv[1])  # sys.argv es una lista que contiene los argumentos de la línea de comandos. El primer elemento (sys.argv[0]) es el nombre del script, y los siguientes elementos son los argumentos proporcionados por el usuario.ejemplo: python Command-line-Arguments.py Alice

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")  # sys.exit() se utiliza para salir del programa. Si se proporciona un mensaje como argumento, se imprimirá antes de salir. En este caso, si el usuario no proporciona al menos un argumento (además del nombre del script), el programa imprimirá "Too few arguments" y luego se cerrará.
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")  # Si el usuario proporciona más de un argumento, el programa imprimirá "Too many arguments" y luego se cerrará.
# else:
#     print("Hello, my name is", sys.argv[1])  # Si el número de argumentos es correcto (exactamente uno), el programa imprimirá el mensaje de saludo con el nombre proporcionado por el usuario.

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, My name is", arg)  # Imprime cada argumento proporcionado por el usuario, incluyendo el nombre del script (sys.argv[0]) y cualquier argumento adicional (sys.argv[1], sys.argv[2], etc.).