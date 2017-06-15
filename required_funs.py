import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from optional_funs import * # I tvivl om hvad der skal imporeres til hvilke filer

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



