import pandas as pd

def CSV(file, name):
    csv = pd.read_csv(file)
    print(f'Salvo em {name}.xlsx')
    return csv.to_excel(f'{name}.xlsx',index = None, header = True)
    

def EXCEL(file, name):
    excel = pd.read_excel(file)
    print(f'Salvo em {name}.csv')
    return excel.to_csv(f'{name}.csv', index= None, header= True)
