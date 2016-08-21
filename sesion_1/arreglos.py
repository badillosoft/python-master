def promedio(arr):
    n = len(arr)

    s = 0
    for x in arr:
        s += x

    return float(s) / n

print promedio([1, 2, 3, 4, 5, 6])

a = [9, 8, 7, 6, 5]

print promedio(a)