import PySimpleGUI as sg
from feetconverter import convert

label1 = sg.Text("Enter feet:")
label2 = sg.Text("Enter Inches:")
feet = sg.InputText(tooltip="Enter feet: ", key="feet")
Inches = sg.InputText(tooltip="Enter Inches: ", key="Inches")
convert_button = sg.Button("Convert")
output = sg.Text(key="output")

window = sg.Window("Convertor", layout=[[label1, feet]
                                       , [label2, Inches],
                                       [convert_button] , [output]])

while True:
    event, values = window.read()
    f = int(values['feet'])
    i = int(values['Inches'])
    output = convert(f, i)
    window["output"].update(value=output)

'''print(event, values)
print(values)
print(values['feet'])
print(output)'''

window.close()
