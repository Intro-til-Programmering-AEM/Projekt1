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
print(dataLoad("test.txt"))

def f(noget):
    return  noget > 10 and noget < 60 
    
f(data.Temperature)

 #list(filter(lambda t: t > 10 and t < 60,data.Temperature))

for 
=======
=======
>>>>>>> f74981612c6f2bdbe8b92b5103e9c5d3185fbb80
bacteria_types = {
    1: "Salmonella enterica",
    2: "Bacillus cereus",
    3: "Listeria",
    4: "Brochothrix thermosphacta"
}
<<<<<<< HEAD
>>>>>>> f74981612c6f2bdbe8b92b5103e9c5d3185fbb80
=======
>>>>>>> f74981612c6f2bdbe8b92b5103e9c5d3185fbb80
