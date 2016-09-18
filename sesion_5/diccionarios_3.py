def circulo(**opciones):
    if not "y" in opciones:
        opciones["y"] = 0 
    print opciones["radio"]
    print opciones["x"]
    print opciones["y"]
    print opciones["color"]

'''circulo({
    "radio": 10,
    "x": 5,
    "y": 3,
    "color": "red"
})'''

circulo(x = 5, radio = 10, color = "red")

a = { "radio": 5, "x": 3, "y": 9, "color": "blue" }

circulo(**a)

'''def dibuja(**kargs):
    if kargs["tipo"] == "circulo":
        circulo(**kargs)

dibuja(tipo = "cuadrado", lado = 5, x = 3, y = 9)
dibuja(circulo = "ciruclo", radio = 5, x = 3, y = 9)'''




