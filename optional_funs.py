import matplotlib.pyplot as plt
#import numpy as np

bacteria_types = {
    1: "Salmonella enterica",
    2: "Bacillus cereus",
    3: "Listeria",
    4: "Brochothrix thermosphacta"
}

def boxPlotGrowthRates(data):
    labels = list(bacteria_types.values())
    values = [[] for i in bacteria_types]
    for i, r in data.iterrows():
        values[int(r.Bacteria) - 1].append(r.GrowthRate)
    plt.figure
    plt.boxplot(values, labels = labels)
    plt.show()
    
def boxPlotTemperatures(data):
	 labels = [bacteria_types[i] for i in set(data.Bacteria)]
	 values = [[] for i in bacteria_types]
    for i, r in data.iterrows():
        values[int(r.Bacteria) - 1].append(r.Temperature)
    plt.figure
    plt.boxplot(values, labels = labels)
    plt.show()
