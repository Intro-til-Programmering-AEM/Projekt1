# Filhåndtering:
import pandas as pd
from inputhandlers import input_wrapper
from data_descriptions import bacteria_types
from os import path

# Denne funktion loader den ønskede fil og frasorterer de data, der ikke opstiller kravene.
def dataLoad(filename): #Det antages, at filen findes
    # Filen indlæses og der gives navne til de tre søjler
    try:
        data=pd.read_csv(filename,sep=' ',names = ["Temperature","GrowthRate", "Bacteria"])
    except:
        return None
    # Der oprettes en tom liste
    toBeDeleted = set()
    # for loop med antallet af rækker
    for i, row in data.iterrows():
        ln = i+1
        # Følgende if-statements sorteres ift. de givne parametre og de værdier, der ikke opfylder kravene kommer i toBeDeleted
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
    # toBeDeleted slettes
    data = data.drop(toBeDeleted)
    return data

# Denne funktion kontrollerer om der er data eller ej.
def input_datafile():
    while(True):
        # Tager filen
        filename = input_filename()
        if filename is None:
            return None
        # Kalder data fra dataLoad
        data = dataLoad(filename)
        if data is not None:
            return data
        # Hvis der ikke er data så kommer der fejlmeddelelse
        else:
            print("File contents are invalid, please try again.")

#
def input_filename():
    while(True):
        try:
            # Modtager fil fra fra input_wrapper
            filename = input_wrapper("Please input the path to your data file: ")
            # Tjekker om filen er en fil
            if path.isfile(filename):
                return(filename)
            else:
                print("File does not exist or you do not have permission to read it. Please try again.")
        except EOFError:
            return None
