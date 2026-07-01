# 1. Introduccion a las Clases en Python
# Las Clases son plantillas para crear objetos. Un objeto es una instancia de una Clase
# Nos permite agrupar datos (atributos o propiedades) y funciones(metodos) en un solo lugar.

# Ejemplo basico de una Clase
# class Coche:
#     # atributo de clase (comparte todas las instancias)
#     tipo = "vehiculo de cuatro ruedas"

#     # metodo especial que es el que construye el objeto
#     # se llama automaticamente este metodo cuando creas las instancias
#     def __init__(self, marca, modelo, color):  # self se refiere asi mismo
#         # atributo de instancia
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def arrancar(self):
#         print(f"El coche {self.marca} {self.modelo} arranco")


# mi_coche = Coche("Toyota", "Corolla", "Rojo")
# tu_coche = Coche("Ford", "Fiesta", "Negro")
# mi_coche.arrancar()  # El coche Toyota Corolla arranco
# tu_coche.arrancar()  # El coche Ford Fiesta arranco

# print(f"{mi_coche} es un {mi_coche.tipo}")

# Encapsulacion: es ocultar los detalles internos de una clase y exponer solo la interfaz publica

# Crear una clase para llamar a la AI de OpenAI, DeepSeek o cual sea
import requests

OPENAI_KEY = "sk-xxxxxxxx"  # Reemplaza con tu clave de API de OpenAI

class API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        # url = "https://api.deepseek.com/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }

        response = requests.post(self.url, json=data, headers=headers)
        res_json = response.json()
        print(res_json["choices"][0]["message"]["content"])
    
openai_api = API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")  

openai_api.call("Escribe un breve poema sobre la programacion")  