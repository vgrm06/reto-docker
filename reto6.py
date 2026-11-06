import mysql.connector
import json

# Leer configuración
with open('config.json') as f:
    config = json.load(f)

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['database']
)

cursor = conexion.cursor()
cursor.execute("SELECT id, marca, modelo, color, km, precio FROM coches")

print("ID   MARCA          MODELO         COLOR      KM      PRECIO")
print("-" * 65)
for (id, marca, modelo, color, km, precio) in cursor:
    print(f"{id:<4} {marca:<14} {modelo:<14} {color:<10} {km:<7} {precio:<8}")

cursor.close()
conexion.close()
