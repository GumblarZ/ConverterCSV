import pandas as pd

def CSV(file):
    csv = pd.read_csv(file)
    return csv.to_excel('file.xlsx',index = None, header = True)

def EXCEL(file):
    excel = pd.read_excel(file)
    return excel.to_csv('file.csv', index= None, header= True)
