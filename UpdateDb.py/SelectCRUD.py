
import PySimpleGUI as sg
import CRUDapp


# Add some colour to the window
sg.theme('DarkTeal9')

layout = [
    [sg.Text('Please select your customer number: ')],
    [sg.Text('Customer Number', size=(15,1)), sg.InputText()],
    [sg.Text('Please select action', size=(15,1)), sg.Combo(['Add', 'Update', 'Delete'])],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(values[0])
        print(values[1])
        if values[1] == 'Add':
            CRUDapp.addData()
        break
window.close()