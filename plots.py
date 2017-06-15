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
    #Hvis filter-listen ikke er tom
    if filters != []:
        plt.title("Filters:"+", ".join(filters))
    plt.show()

#Laver histogram over bakterietyper
def plotNumbers(data):
    #tæller antallet af bakterier
    counts = [list(data.Bacteria).count(i) for i in bacteria_types.keys()]
    #Histogram plot:
    plt.bar(list(bacteria_types.keys()), counts, tick_label = list(bacteria_types.values()))
    plt.title("Numbers of each type of bacteria")
    plt.ylabel("Number of bacteria")

#Plotter growth rates for de forskellige bakterietyper
def plotGrowthRates(data):
    #En tom liste der er ligeså lang som antallet af bakterier
    points = [[] for i in bacteria_types]
    #Loop der behandler hele raekker
    for i, r in data.iterrows():
        #samler temperatur og growthrate som et talpar
        points[int(r.Bacteria) - 1].append((r.Temperature, r.GrowthRate))
        # talpar i en liste af lister ~ [[(temp, growthRate)]]. Nu sorteret efter størrelse
    points = [sorted(pointList,key=lambda t: t[0]) for pointList in points]
    # Skiller talparene ad. Foer havde vi lister af par, men nu har vi par af lister ~ [[(temps),(growthRates)]]
    xyPairList = [zip(*pointList) for pointList in points]
    # Samler listerne i en lister, hvor de er sorteret i x, y, x,y ~ [(temps),(growthRates),(temps),...]
    flattened = [item for pair in xyPairList for item in pair]
    #* betyder at man åbner listen inde i plot-funktionen
    plt.plot(*flattened)
    #label anvendes til legend så den er følsom overfor filtrene
    label = [bacteria_types[i] for i in set(data.Bacteria)] #
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
    plt.title("Boxplot for growth rates")
    plt.boxplot(values, labels = labels)

def boxPlotTemperatures(data):
    labels = list(bacteria_types.values())
    values = [[] for i in bacteria_types]
    for i, r in data.iterrows():
        values[int(r.Bacteria) - 1].append(r.Temperature)
    plt.figure
    plt.title("Boxplot for temperatures")
    plt.boxplot(values, labels = labels)
