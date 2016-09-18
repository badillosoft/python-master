import json

f = open("sesion.txt", mode = "r")

data = f.readline()

dic = json.loads(data)

print "x", dic["x"]