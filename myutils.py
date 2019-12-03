import os
import matplotlib.pyplot as plt

def mySaveFig(filename):
    try:
        plt.savefig(filename)
    except FileNotFoundError:
        directoryName = os.path.dirname(filename)
        os.mkdir(directoryName)
        plt.savefig(filename)
    