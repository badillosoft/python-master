def f(x):
    if x <= 1:
        return x
    
    return x ** 2

x = -5
while x <= 5:
    print x, f(x)

    x += 0.1