# Como hacer peticiones a APIs con Python
# Con y sin dependencias

# Forma dificil y sin dependencias

# 1. Sin dependencias
# import urllib.requests
# import json

# Llamamos a la api
# api_posts = "https://jsonplaceholder.typicode.com/posts"

# try: # Es buena practica poner todo dentro de un try
#     # respuesta de la pagina/api
#     response = urllib.request.urlopen(api_posts)

#     # Lea los datos de esa respuesta
#     data = response.read()

#     # Decodificar los datos JSON y los cargue
#     json_data = json.loads(data.decode('utf-8'))
#     print(json_data)

#     # Cerramos la llamada con la api
#     response.close()
# except urllib.error.URLError as e:
#     print(f"Erorr en la solicitud: {e}")

# 2. Con dependencia (requests)
# import requests
# import json

# print("\nGET:")
# api_posts = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(api_posts)
# print(response.json())

# # Una vez obtenido todos los datos ya somos capaces de interactuar con ellos
# response_json = response.json()
# print(response_json[0])

# # 3. Hacer un POST
# print("\nPOST:")
# try:
#     api_posts = "https://jsonplaceholder.typicode.com/posts"
#     input = {"userId": 1, "title": "NBA", "body": "cuerpo"}
#     response = requests.post(api_posts, json=input)
#     print(response.json())
#     print(
#         response.status_code
#     )  # con esta linea podemos saber como esta funcionando el codigo, si tira/devuelve el codigo 201 es porque funciona bien
# except requests.exceptions.ReguesException as e:
#     print(f"Error en la solicitud: {e}")

# # 4 un PUT
# print("\nPUT:")
# try:
#     api_posts = "https://jsonplaceholder.typicode.com/posts/1"  # Hay que ir a la url del objeto que queremos agregar/actualizar algo
#     input = {
#         "userId": 1,
#         "title": "NBA",
#         "body": "cuerpo",
#     }
#     response = requests.put(api_posts, json=input)
#     print(response.json())
#     print(
#         response.status_code
#     )  # con esta linea podemos saber como esta funcionando el codigo, si tira/devuelve el codigo 201 es porque funciona bien
# except requests.exceptions.ReguesException as e:
#     print(f"Error en la solicitud: {e}")

# Usar la API de GPT-4o de OpenAI
# ref: https://api.openai.com/v1/chat/completions
# API Key: xxxx

# import requests
# import json

# print("\nUsar la API de GPT-4o de OpenAI")

# OPENAI_KEY = "sk-proj-xxxxxxx"  # Reemplaza con tu clave de API de OpenAI

# def call_openai_gpt(api_key, prompt):
#     url = "https://api.openai.com/v1/chat/completions"
#     headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
#     data = {
#         "model": "gpt-4o-mini",
#         "messages": [{"role": "user", "content": prompt}],
#     }

#     response = requests.post(url, json=data, headers=headers)
#     return response.json()


# api_response = call_openai_gpt(
#     OPENAI_KEY, "Escribe un breve poema sobre la programacion"
# )
# # print(json.dumps(api_response, indent=2))
# print(api_response["choices"][0]["message"]["content"])
# # ---------------------------------------------------------------

# # Llamar la API de DeepSeek
# print("\nUsar la API de DeepSeek")

# deepseek_KEY = "sk-xxxxxxxx"  # Reemplaza con tu clave de API de DeepSeek


# def call_deepseek(api_key, prompt):
#     url = "https://api.deepseek.com/chat/completions"
#     headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
#     data = {
#         "model": "deepseek-v4-flash",
#         "messages": [{"role": "user", "content": prompt}],
#     }

#     response = requests.post(url, json=data, headers=headers)
#     return response.json()


# api_response = call_deepseek(
#     deepseek_KEY, "Escribe un breve poema sobre la programacion"
# )
# # print(json.dumps(api_response, indent=2))
# print(api_response["choices"][0]["message"]["content"])


# ---------------------------------------------------------------

# Llamar la API de Claude
import requests

print("\nUsar la API de Claude")

claude_KEY = "sk-xxxxxxxx"  # Reemplaza con tu clave de API de Claude


def call_claude(api_key, prompt):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    data = {
        "model": "claude-haiku-4-5",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()


api_response = call_claude(claude_KEY, "Escribe un breve poema sobre la programacion")
print(api_response)
# print(json.dumps(api_response, indent=2))
print(api_response["content"][0]["text"])