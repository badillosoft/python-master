data = [
    [1, 5, 6, 8, 4],
    [1, 5, 6, 8, 4],
    [1, 5, 6, 8, 4],
    [1, 5, 6, 8, 4],
    [1, 5, 6, 8, 4]
]

f = open("data.csv", mode = "w")

for row in data:
    f.write(", ".join([str(x) for x in row]))
    f.write(";\n")

f.close()