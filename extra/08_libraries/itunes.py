
import requests
import sys
import os

os.system("cls")  # Limpiar la consola (en Windows)

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])  # Realiza una solicitud GET a la API de iTunes para buscar canciones relacionadas con el término proporcionado por el usuario. El parámetro "entity=song" especifica que solo se buscan canciones, "limit=50" limita los resultados a 50 canciones, y "term=" seguido del argumento del usuario especifica el término de búsqueda.

o = response.json()  # Convierte la respuesta de la API de iTunes en un objeto JSON que se puede manipular en Python.

for result in o["results"]:
    print(result["trackName"])  # Itera a través de los resultados obtenidos de la API de iTunes y imprime el nombre de cada canción (trackName) en la consola.