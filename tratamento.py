from tkinter import filedialog as fd
import os
import Convert

file = fd.askopenfilename()

name = os.path.splitext(file)

if(name[1] == '.xlsx'):
    Convert.EXCEL(file)

if(name[1] == '.csv'):
    Convert.CSV(file)

