import pandas as pd
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
        if(row.Bacteria not in bacteria_types.keys):
            toBeDeleted.add(i)
            print("Bacteria type not valid in line"+str(ln))
    data = data.drop(toBeDeleted)
    print(data)
    return data 


def dataStatistics(data, statistic):
    print("Error: not implemented yet") # TODO

def dataPlot(data):
    print("Error: not implemented yet") # TODO
