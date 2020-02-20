
import PySimpleGUI as sg

num = 5

stable_1 = [[sg.Text("",size=(10,1), key="1" + str(i))] for i in range(1, num)]
stable_2 = [[sg.Text("",size=(10,1), key="2" + str(i))] for i in range(1, num)]

hand_1 = [[sg.Text("",size=(10,1), key="1" + str(i))] for i in range(1, num)]
hand_2= [[sg.Text("",size=(10,1), key="2" + str(i))] for i in range(1, num)]


col = [
        [sg.Button('Unicorn', key = "-UNI-")],
        [sg.Button('Magic', key = "-MAG-")],
        [sg.Button('Upgrade', key = "-UP-")],
        [sg.Button('Downgrade', key = "-DOWN-")],
        [sg.Button('Instant', key = "-INST-")],
       ]


layout = [
          [sg.Column(col),
           sg.Frame('STABLE 1', stable_1, font='Any 12', title_color='blue'),
           sg.Frame('STABLE 2', stable_2, font='Any 12', title_color='blue')],

         [sg.Frame('HAND 1', hand_1, font='Any 12', title_color='blue'),
           sg.Frame('HAND 2', hand_2, font='Any 12', title_color='blue'),
         sg.Text("It's Your Turn, Naomi", size=(15,1))]
         ]

window = sg.Window('Frame with buttons', layout, font=("Helvetica", 12))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in  (None, 'Exit'):
        break
    if event == '-UNI-':
        # Update the "output" text element to be the value of "input" element
        window['11'].update("Unicorn")
    if event == '-MAG-':
        # Update the "output" text element to be the value of "input" element
        window['11'].update("Gone")

window.close()


