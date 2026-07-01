import sys
from PIL import Image
import os
os.system("cls")  # Limpiar la consola (en Windows)

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "costumer.gif", save_all=True, append_images=[images[1]], duration=20, loop=0                                      
) 