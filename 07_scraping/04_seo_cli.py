from bs4 import BeautifulSoup
from urllib.parse import urljoin

import requests
import argparse

parser = argparse.ArgumentParser(description="Web scraping to check SEO for a given URL")
parser.add_argument("url", type=str, help="The URL of the site you want to scrape and check")
args = parser.parse_args()
url = args.url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding = "utf-8"
   
if response.status_code == 200:
    print("La peticion fue exitosa")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    print(f"Revisando la pagina: {url}")
    print("\SEO basico:")
    
    titulo_pagina = soup.find("title").get_text()
    
    if titulo_pagina:
        print(f"\033[46mTitulo de la pagina: {titulo_pagina}\033[0m")
    
        if len(titulo_pagina) < 70:
            print("\033[32mEl titulo de la pagina es adecuado para SEO\033[0m")
        elif len(titulo_pagina) > 70:
            print("El titulo de la pagina es demasiado largo para SEO")
    
    # Extrae todos los titulos h1
    titulos = [titulo.text for titulo in soup.find_all("h1")]
    if not titulos:
        print("\033[31mNo se encontraron titulos h1 en la pagina\033[0m")
    elif len(titulos) > 1:
        print("\033[31mSe encontraron mas de un titulo h1 en la pagina\033[0m")
        for titulo in titulos:
            print(titulo)
    else:
        print(f"\033[32mSe encontro un titulo h1 en la pagina: {titulos[0]}\033[0m")
