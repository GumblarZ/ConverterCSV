from tkinter import filedialog as fd
import pandas as pd

try: 
    file = fd.askopenfilename()
except KeyError:
    print(KeyError)

print(file)
csv = pd.read_csv(file)
csv.to_excel('virou.xlsx',index = None, header = True)
