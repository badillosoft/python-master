import json

def seve_dic(fname, dic):
    f = open(fname, mode = "w")

    f.write(json.dumps(dic))

    f.close()

def load_dic(fname):
    f = open(fname, mode = "r")

    data = f.readline()

    f.close()

    dic = json.loads(data)

save_dic("sesion_2.json", { "a":8, "b": 32 })

dic = load_dic("sesion.txt")