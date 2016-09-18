import json

dic = {
    "x": 0,
    "y": 2,
    "data": [1, 5, 6, 7],
    "promedio": 4.78,
    "flag_1": True,
    "flag_2": False
}

f = open("sesion.txt", mode = "w")

f.write(json.dumps(dic))

f.close()