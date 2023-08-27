import PySimpleGUI as sg

def addData():   
    sg.theme('DarkTeal9')  # Add some colour to the window
    layout = [
        [sg.Text('Please fill out the following fields: ')],
        [sg.Text('Customer Number', size=(15,1)), sg.InputText()],
        [sg.Text('Customer Name', size=(15,1)), sg.InputText()],
        [sg.Text('Street', size=(15,1)), sg.InputText()],
        [sg.Text('City', size=(15,1)), sg.InputText()],
        [sg.Text('State', size=(15,1)), sg.InputText()],
        [sg.Text('Zip', size=(15,1)), sg.InputText()],
        [sg.Text('Balance', size=(15,1)), sg.InputText()],    
        [sg.Text('Credit Limit', size=(15,1)), sg.InputText()],
        [sg.Text('Rep Number', size=(15,1)), sg.InputText()],
        [sg.Submit(), sg.Exit()]
    ]
    window = sg.Window('Simple data entry form', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Submit':
            CustomerNum = values[0]
            CustomerName = values[1]
            Street = values[2]
            City = values[3]
            State = values[4]
            Zip = values[5]
            Balance = values[6]
            CreditLimit = values[7]
            RepNum = values[8]
            print(values)
            return(values)       
            break
    window.close()

