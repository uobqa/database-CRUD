
import PySimpleGUI as sg

# Add some colour to the window
sg.theme('DarkTeal9')

layout = [
    [sg.Text('Please fill out the following fields: ')],
    [sg.Text('First Name', size=(15,1)), sg.InputText()],
    [sg.Text('Second Name', size=(15,1)), sg.InputText(key='SName')],
    [sg.Text('Favourite colour', size=(15,1)), sg.Combo(['Red', 'Blue', 'Green'], key='Favouritecolour')],
    [sg.Text('I speak', size=(15,1)),
                            sg.Checkbox('English', key='English'),
                            sg.Checkbox('Spanish', key='Spanish'),
                            sg.Checkbox('German', key='German')],
    [sg.Text('No. of children', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                        initial_value=0, key='Children')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(values[0])
        break
window.close()