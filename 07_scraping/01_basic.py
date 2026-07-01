# pip3 install requests -> instalas la dependencia para hacer peticiones

# Scraping de webs
# 1. requests

import requests
import re

url = 'https://books.toscrape.com/'

response = requests.get(url)
response.encoding = 'utf-8'

if response.status_code == 200:
    print ("La peticion fue exitosa")
    html = (response.text)
    
    # regular expression para encontrar el precio
    price_pattern = r'<p class="price_color">(.*?)</p>'
    
    match = re.search(price_pattern, html)
    
    if match:
        print(f"El precio del producto es: {match.group(1)}")
