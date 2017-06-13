import pandas as pd
def dataLoad(filename): #Det antages, at filen findes
    try:    
        data=pd.read_csv(filename,sep=' ')
        return data
    except:
        return None

def dataStatistics(data, statistic):
    print("Error: not implemented yet") # TODO

def dataPlot(data):
    print("Error: not implemented yet") # TODO
