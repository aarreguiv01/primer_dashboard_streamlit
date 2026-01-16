import csv
import time
import datetime
import random
import os

# Crea el archivo con cabecera si no existe
if not os.path.exists('log.csv'):
    with open('log.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "valor"])

print("Generando datos cada 2 segundos... (Presiona Ctrl+C para detener)")

while True:
    with open('log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        valor = random.randint(10, 50) # Genera un número aleatorio
        writer.writerow([ahora, valor])
        print(f"Dato insertado: {ahora}, {valor}")
    
    time.sleep(2) # Espera 2 segundos antes de la siguiente fila