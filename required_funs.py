import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

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
            print("Growth rate not positive in line"+str(ln))
        if(row.Bacteria not in bacteria_types.keys()):
            toBeDeleted.add(i)
            print("Bacteria type not valid in line"+str(ln))
    data = data.drop(toBeDeleted)
    print(data)
    return data


def dataStatistics(data, statistic):
    if statistic=="Mean Temperature":
        gns_Temperatur=np.mean(data.Temperature)
        return gns_Temperatur
    if statistic=="Mean GrowthRate":
        gns_GR=np.mean(data.GrowthRate)
        return gns_GR
    if statistic=="Std Temperature":
        std_Temperatur=np.sd(data.Temperature)
        return std_Temperatur
    if statistic=="Std GrowthRate":
        std_GR==np.sd(data.GrowthRate)
        return std_GR
    if statistic=="Rows":
        return(len(data))
    if statistic=="Mean Cold Growth Rate":
        gns_cold=np.mean(data.GrowthRate[data.Temperature<20])
        return gns_cold
    if statistic=="Mean Hot Growth Rate":
        gns_hot=np.mean(data.GrowthRate[data.Temperature>50])
        return gns_hot



def dataPlot(data):
    plotNumbers(data)
    plotGrowthRates(data)

def plotNumbers(data):
    counts = [1,2,3,1]
    plt.bar(list(bacteria_types.keys()), counts, tick_label = list(bacteria_types.values()))
    plt.title("Numbers of each type of bacteria")
    plt.ylabel("Number of bacteria")
    plt.show()

def plotGrowthRates(data):
    print("Error: not implemented yet") # TODO

bacteria_types = {
    1: "Salmonella enterica",
    2: "Bacillus cereus",
    3: "Listeria",
    4: "Brochothrix thermosphacta"
}
