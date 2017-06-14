import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bacteria_types = {
    1: "Salmonella enterica",
    2: "Bacillus cereus",
    3: "Listeria",
    4: "Brochothrix thermosphacta"
}

def dataLoad(filename): #Det antages, at filen findes
    try:
        data=pd.read_csv(filename,sep=' ',names = ["Temperature","GrowthRate", "Bacteria"])
    except:
        return None
    toBeDeleted = set()
    for i, row in data.iterrows():
        ln = i+1
        if(row.Temperature < 10):
            toBeDeleted.add(i)
            print("Temperature too low in line "+str(ln))
        if(row.Temperature > 60):
            toBeDeleted.add(i)
            print("Temperature too high in line "+str(ln))
        if(row.GrowthRate < 0):
            toBeDeleted.add(i)
            print("Growth rate not positive in line "+str(ln))
        if(row.Bacteria not in bacteria_types.keys()):
            toBeDeleted.add(i)
            print("Bacteria type not valid in line "+str(ln))
    data = data.drop(toBeDeleted)
    return data

def dataStatistics(data, statistic):
    if statistic == "Mean Temperature":
        return np.mean(data.Temperature)
    elif statistic == "Mean Growth rate":
        return np.mean(data.GrowthRate)
    elif statistic == "Std Temperature":
        return np.sd(data.Temperature)
    elif statistic == "Std Growth rate":
        return np.sd(data.GrowthRate)
    elif statistic == "Rows":
        return(len(data))
    elif statistic == "Mean Cold Growth rate":
        return np.mean(data.GrowthRate[data.Temperature<20])
    elif statistic == "Mean Hot Growth rate":
        return np.mean(data.GrowthRate[data.Temperature>50])

def dataPlot(data):
    plotNumbers(data)
    plotGrowthRates(data)

def plotNumbers(data):
    counts = [list(data.Bacteria).count(i) for i in bacteria_types.keys()]
    plt.bar(list(bacteria_types.keys()), counts, tick_label = list(bacteria_types.values()))
    plt.title("Numbers of each type of bacteria")
    plt.ylabel("Number of bacteria")
    plt.show()

def plotGrowthRates(data):
    points = [[] for i in bacteria_types]
    for i, r in data.iterrows():
        points[int(r.Bacteria) - 1].append((r.Temperature, r.GrowthRate))
    points = [sorted(pointList,key=lambda t: t[0]) for pointList in points] # [[(temp, growthRate)]]
    xyPairList = [zip(*pointList) for pointList in points] # [[(temps),(growthRates)]]
    flattened = [item for pair in xyPairList for item in pair] # [(temps),(growthRates),(temps),...]
    plt.plot(*flattened)
    label=(list(bacteria_types.values()))
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.grid()
    plt.title("Growth rate by temperature")
    plt.legend(label,loc="upper right")
    plt.xlim(10,60)
    plt.ylim(ymin=0)
    plt.show()