import numpy as np

#Nedenstående funktion laver de statistik-funktioner, der er krævet i oplægget:
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

