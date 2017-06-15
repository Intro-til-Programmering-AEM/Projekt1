#Filhåndtering:
import pandas as pd
from required_funs import bacteria_types
from inputhandlers import input_wrapper
from os import path

#Denne funktion loader den ønskede fil og frasorterer de data, der ikke opstiller kravene.
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

#Denne funktion kontrollerer om der er data eller ej.
def input_datafile():
    while(True):
        filename = input_filename()
        if filename is None:
            return None
        data = dataLoad(filename)
        if data is not None:
            return data
        else:
            print("File contents are invalid, please try again.")

#
def input_filename():
    while(True):
        try:
            filename = input_wrapper("Please input the path to your data file: ")
            if path.isfile(filename):
                return(filename)
            else:
                print("File does not exist or you do not have permission to read it. Please try again.")
        except EOFError:
            return None