from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

headers = {
   'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.get(url)
response.encoding = "utf-8"

if response.status_code == 200:
    # print("La peticion fue exitosa")

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    title_tag = soup.title

    if title_tag:
        print(f"El titulo de la web es: {title_tag.text}")
    else:
        print("Error con el titulo")

    # find price using bs
    # price_span = soup.find("p", class_="price_color")
    # if price_span:
    #     print(f"El precio del producto es: {price_span.text}")
    # else:
    #     print("Error con el precio")

    # find all the prices
    # Una forma
    # name_all_span = soup.find_all("a", title=True)
    # price_all_span = soup.find_all("p", class_="price_color")
    
    # for price, name in zip(price_all_span, name_all_span):
    #     if price_all_span and name_all_span:
    #         print(f"Libro: {name.text}")
    #         print(f"Precio: {price.text}")
    #     else:
    #         print("Error con el precio")

    # Otra forma
    products = soup.find_all(class_="product_pod")

    for product in products:
        name = product.find("a", title=True)
        price = product.find("p", class_="price_color")
        print(f"El libro {name.text} tiene un precio de {price.text}")
