import pandas

file = #file CSV#

csv = pandas.read_csv(file)
csv.to_excel('new.xlsx',index = None, header = True)
