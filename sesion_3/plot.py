import matplotlib.pyplot as plot

for x in range(0, 10):
    for y in range(0, 10):
        plot.clf()
        plot.axis([0, 10, 0, 10])
        plot.autoscale(False) 
        plot.scatter(x, y)
        plot.pause(0.001)

raw_input()