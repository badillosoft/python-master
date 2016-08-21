g = 9.81

x0 = float(raw_input("Dame x0: "))
y0 = float(raw_input("Dame y0: "))

vx0 = float(raw_input("Dame vx0: "))
vy0 = float(raw_input("Dame vy0: "))

t_max = int(raw_input("Dame el tiempo maximo: "))

t = 0
while t <= t_max:
    x = x0 + vx0 * t
    y = y0 + vy0 * t - (g * t ** 2.0) / 2.0

    print x, ',', y

    t = t + 0.2