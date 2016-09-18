import sqlite3

conn = sqlite3.connect("pokemon.db")

c = conn.cursor()

# Creamos la tabla de entrenadores pokemon :)
print "Creando tabla entranadores"
c.execute("CREATE TABLE IF NOT EXISTS entrenadores (id INT AUTO_INCREMENT, nombre VARCHAR(60), sexo VARCHAR(1))")

conn.commit()

c.close()