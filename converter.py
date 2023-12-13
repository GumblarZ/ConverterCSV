import pandas

def CSV(file):
    csv = pandas.read_csv(file)
    return csv.to_excel('new.xlsx',index = None, header = True)

def Excel(file):
    Excel = pandas.read_excel(file)
    return Excel.to_csv('new.csv')
