f = open("data.txt", mode = "w")

f.writelines([
    "Hola\n",
    "mundo"
])

f.write(" :)")

f.close()