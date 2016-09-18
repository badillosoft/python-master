dic = {
    "rojo": 1,
    "manzana": ("roja", "chica"),
    "clave": "valor"
}

print "rojo:", dic["rojo"]
print "manzana:", dic["manzana"]
print "clave:", dic["clave"]
#print "foo:", dic["foo"] # Error: la clave no existe en el dic

dic["foo"] = 12.34

print "foo:", dic["foo"]

for k in dic:
    print "Llave:", k, "Valor:", dic[k]

def get_keys(dic):
    keys = []

    for k in dic:
        keys.append(k)

    return keys
    #return [k for k in dic]

print get_keys(dic)

print [x**2 for x in range(1, 11)]
print [2 * x + 1 for x in range(0, 11)]