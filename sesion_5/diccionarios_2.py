def suma(*arr):
    s = 0
    for x in arr:
        s += x
    return s

print suma(4, 6, 9)
print suma(1, 2)
print suma(1, 2, 3, 4, 5, 6, 7, 8, 50)
print suma(*[1, 5, 6])