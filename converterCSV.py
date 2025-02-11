from tkinter import filedialog as fd
import pandas as pd

file = fd.askopenfilename()

filename = file 
print(file)

excel = pd.read_excel(file)
excel.to_csv('pizza.csv' , index= None, header= True)

#pegar o arquivo e converter pra csv