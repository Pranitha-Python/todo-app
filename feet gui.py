import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
label2 = sg.Text("Enter Inches:")
feet = sg.InputText(tooltip="Enter feet: ")
Inches = sg.InputText(tooltip="Enter Inches: ")
convert_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label1, feet]
                                     , [label2, Inches],
                                       [convert_button]])
window.read()
window.close()