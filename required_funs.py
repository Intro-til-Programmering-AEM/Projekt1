import pandas as pd
import os 



def dataLoad(filename): #Det antages, at filen findes
    try:    
        data=pd.read_csv(filename,sep=' ',names = ["Temperature","Growth rate", "Bacteria"])
    except:
        return None
    return data 

def dataStatistics(data, statistic):
    print("Error: not implemented yet") # TODO

def dataPlot(data):
    print("Error: not implemented yet") # TODO

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
print(dataLoad("test.txt"))

def f(noget):
    return  noget > 10 and noget < 60 
    
f(data.Temperature)

 #list(filter(lambda t: t > 10 and t < 60,data.Temperature))


