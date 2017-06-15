#Denne fil indeholder plots og plot relaterede funktioner
import matplotlib.pyplot as plt
from required_funs import bacteria_types
#Nedenstående funktion anvender plotwrapper funktionen på de andre plotfunktioner
def dataPlot(data,filters=[]):
    plotWrapper(plotNumbers, data, filters)
    plotWrapper(plotGrowthRates, data, filters)
    plotWrapper(boxPlotGrowthRates, data, filters)
    plotWrapper(boxPlotTemperatures, data, filters)

#plotWrapper funktionen tilføjer de valgte filtre til graf-titlen
def plotWrapper(plotFun,data, filters):
    plotFun(data)
    if filters != []:
        plt.title("Filters:"+", ".join(filters))
    plt.show()

#Laver histogram over bakterietyper
def plotNumbers(data):
    counts = [list(data.Bacteria).count(i) for i in bacteria_types.keys()]
    plt.bar(list(bacteria_types.keys()), counts, tick_label = list(bacteria_types.values()))
    plt.title("Numbers of each type of bacteria")
    plt.ylabel("Number of bacteria")

def plotGrowthRates(data):
    points = [[] for i in bacteria_types]
    for i, r in data.iterrows():
        points[int(r.Bacteria) - 1].append((r.Temperature, r.GrowthRate))
    points = [sorted(pointList,key=lambda t: t[0]) for pointList in points] # [[(temp, growthRate)]]
    xyPairList = [zip(*pointList) for pointList in points] # [[(temps),(growthRates)]]
    flattened = [item for pair in xyPairList for item in pair] # [(temps),(growthRates),(temps),...]
    plt.plot(*flattened)
    label = [bacteria_types[i] for i in set(data.Bacteria)]
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.grid()
    plt.suptitle("Growth rate by temperature")
    plt.legend(label,loc="upper right")
    plt.xlim(10,60)
    plt.ylim(ymin=0)

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

