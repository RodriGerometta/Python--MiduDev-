# Trabajando con fechas y horas en python

import os

os.system("cls")

from datetime import datetime, timedelta

# 1. Obtener la fehca y la hora actual
# now = datetime.now()
# print(f"Fecha y hora actual: {now}")

# 2. Crear una fecha y hora especifica
# specific_date = datetime(2025, 12, 13)
# print(f"Fecha y hora especifica: {specific_date}")

# 3. Formatear fechas
# metodo strftime() para formatear fechas
# pasale el objerto datetime y el formato especificado
# formato:
# format_date = now.strftime("%d/%m/%Y")
# print(f"Fecha formateada: {format_date}")

# 4. Operaciones con fechas (sumar, restar dias, minutos, horas, meses, etc)

# yesterday = datetime.now() - timedelta(days=1)
# print(f"Ayer fue: {yesterday}")
# semana_pasada = datetime.now() - timedelta(weeks=1)
# print(f"La semana pasada fue: {semana_pasada}")
# tomorrow = datetime.now() + timedelta(days=1)
# print(f"Mañana seria: {tomorrow}")

# 5. Obtener componentes individuales de una fecha
# now = datetime.now()
# year = now.year
# print(year)

# month = now.month
# print(month)

# # 6. Calcular la diferencia entre 2 fechas
# date1 = datetime.now()
# print(date1)
# date2 = datetime(2026, 12, 13)
# difference = date2-date1
# print(f"La diferencia entre las fehcas: {difference}")

# importamos locale
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

now = datetime.now()
current_day = now.strftime("%A/%B/%Y")
print(current_day)