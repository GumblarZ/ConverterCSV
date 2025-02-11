import pandas as pd

def CSV(file, name):
    csv = pd.read_csv(file)
    return csv.to_excel(f'{name}.xlsx',index = None, header = True)

def EXCEL(file, name):
    excel = pd.read_excel(file)
    return excel.to_csv(f'{name}.csv', index= None, header= True)
