import matplotlib.pyplot as plt
#import numpy as np
from required_funs import *


def boxPlotGrowthRates(data):
    labels = list(bacteria_types.values())
    values = [[] for i in bacteria_types]
    for i, r in data.iterrows():
        values[int(r.Bacteria) - 1].append(r.GrowthRate)
    plt.figure
    plt.boxplot(values, labels = labels)

def boxPlotTemperatures(data):
	 labels = [bacteria_types[i] for i in set(data.Bacteria)]
	 values = [[] for i in bacteria_types]
    for i, r in data.iterrows():
        values[int(r.Bacteria) - 1].append(r.Temperature)
    plt.figure
    plt.boxplot(values, labels = labels)

