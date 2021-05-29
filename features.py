import pandas as pd
import numpy as np


df2=pd.read_csv(r"C:\Users\dhaval.panchal\Pictures\cars_categorization\Training_CSV_File/training_file.csv",encoding= 'unicode_escape')

df2.columns =[column.replace(" ", "_") for column in df2.columns]

options =['petrol','cng','diesel','sunroof','climate_control']

for i in range(len(options)):
    print(str(i+1) + ":", options[i])

inp = int(input("Enter your choice pecification: "))
if inp in range(1, 7):
    inp = options[inp-1]
    if inp=='petrol':
        df2.query("petrol == True", inplace = True)
        newaa=df2["car_model"]
        print(f'{newaa}')
    if inp=='cng':
        df2.query("cng == True", inplace = True)
        newaa=df2["car_model"]
        print(f'{newaa}')
    if inp=='diesel':
        df2.query("diesel == True", inplace = True)
        newaa=df2["car_model"]
        print(f'{newaa}')
    if inp=='sunroof':
        df2.query("roof == True", inplace = True)
        newaa=df2["car_model"]
        print(f'{newaa}')
    if inp=='climate_control':
        df2.query("climate_control == True", inplace = True)
        newaa=df2["car_model"]
        print(f'{newaa}')


else:
    print("Invalid input!")
