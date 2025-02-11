from tkinter import filedialog as fd
import pandas as pd
import os

file = fd.askopenfilename()

name = os.path.splitext(file)

if(name[1] == '.xlsx'):
    excel = pd.read_excel(file)
    excel.to_csv('pizza.csv' , index= None, header= True)

if(name[1] == '.csv'):
    csv = pd.read_csv(file)
    csv.to_excel('virou.xlsx',index = None, header = True)

