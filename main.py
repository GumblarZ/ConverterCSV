from tkinter import filedialog
import converter

file = filedialog.askopenfilename()

dialog = input("opção \na) Excel para CSV \nb) CSV para excel \n ")

if(dialog == 'a'):
    converter.Excel(file)
if(dialog == 'b'):
    converter.CSV(file)
