import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plotter(func):
    costs = []
    def inner_plotter(*args,**kwargs):
        cost = func(*args,**kwargs)
        costs.append(cost)
        plt.plot(costs)
        plt.pause(0.05)
        return cost
    return inner_plotter
