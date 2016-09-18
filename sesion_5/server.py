import bottle
import time
import sqlite3

conn = sqlite3.connect("pokemon.db")

@bottle.get("/")
def mostrar_entrenadores():
    c = conn.cursor()

    it = c.execute("SELECT * FROM entrenadores")

    return bottle.template("tabla_entrenadores", it = it)

@bottle.get("/hola")
def foo():
    return bottle.template("hello", name = "Ash")

@bottle.get("/time")
def foo1():
    return time.strftime("%Y-%m-%d %H:%M:%S",
        time.gmtime())

@bottle.get("/crear/:nombre/:sexo")
def crear_entrenador(nombre, sexo):
    c = conn.cursor()

    c.execute("INSERT INTO entrenadores (nombre, sexo) VALUES(?, ?)", (nombre, sexo,))

    conn.commit()

    return "Se creo %s (%s)" %(nombre, sexo)

bottle.run(host = "localhost", port = 3000)