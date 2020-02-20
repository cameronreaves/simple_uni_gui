# import PySimpleGUI as sg
#
# #list comprehension [ expression for item in list if conditional ]
# # VerticalSeparator(pad=None)
#
# layout = [ [sg.Txt('Enter values to calculate')],
#             [sg.In(size=(8,1), key='numerator')],
#             [sg.Txt('_'  * 10)],
#             [sg.In(size=(8,1), key='denominator')],
#             [sg.Txt('', size=(8,1), key='output')  ],
#             [sg.Button('Calculate', bind_return_key=True)]]
#
# window = sg.Window('Math', layout)
#
# while True:
#     event, values = window.read()
#
#     if event is not None:
#         try:
#             numerator = float(values['numerator'])
#             denominator = float(values['denominator'])
#             calc = numerator / denominator
#         except:
#             calc = 'Invalid'
#
#         window['output'].update(calc)
#     else:
#         break
#

# import PySimpleGUI as sg
# #
# # # Demo of how columns work
# # # window has on row 1 a vertical slider followed by a COLUMN with 7 rows
# # # Prior to the Column element, this layout was not possible
# # # Columns layouts look identical to window layouts, they are a list of lists of elements.
# #
# # window = sg.Window('Columns')                                   # blank window
# #
# # # Column layout
# # col = [[sg.Text('Unicorn')],
# #         [sg.Text('Magic')],
# #         [sg.Text('Upgrade')],
# #         [sg.Text('Downgrade')],
# #         [sg.Text('Instant')],
# #        ]
# #
# # layout = [[sg.Column(col)],
# #           [sg.Column(col),sg.Column(col)]]
# #
# # # Display the window and get values
# #
# # window = sg.Window('Compact 1-line window with column', layout)
# # event, values = window.read()


import PySimpleGUI as sg

num = 5

stable_1 = [[sg.Text(f'{i}. ', key="1" + str(i))] for i in range(1, 6)]
stable_2 = [[sg.Text(f'{i}. ', key="2" + str(i))] for i in range(1, 6)]


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
           sg.Frame('STABLE 2', stable_2, font='Any 12', title_color='blue')]
         ]

window = sg.Window('Frame with buttons', layout, font=("Helvetica", 12))
window.read()
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





# while True:             # Event Loop
#     event, values = window.read()
# #     if event in (None, 'Exit'):
# #         break
# #     # When choice has been made, then fill in the listbox with the choices
# #     if event == '-UNI-':
# #         window['-F-'].Update("Uni")
# # window.close()


# TABS
# layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
#               [sg.Button('Read')]]


# import PySimpleGUI as sg
# from random import randint
#
# sg.theme('Dark Blue 3')
#
# layout = [  [sg.Text('Temperature'), sg.T(' '*30), sg.Text(size=(8,1), key='-TEMP OUT-')],
#             [sg.Text('Set Temp'), sg.T(' '*8), sg.Input(size=(8,1), key='-IN-'), sg.T(' '*10), sg.Button('Set')],
#             [sg.Button('Off'), sg.T(' '*13), sg.Button('Turn relay on', button_color=('white', 'red')),sg.T(' '*5), sg.Button('Quit')]  ]
#
# window = sg.Window('Temperature Manager', layout, font='Default -24', return_keyboard_events=True, no_titlebar=True)
#
# while True:             # Event Loop
#     event, values = window.read(timeout=500)    # returns every 500 ms
#     print(event, values) if event != sg.TIMEOUT_KEY else None       # a debug print
#     if event in (None, 'Quit'):
#         break
#     if event == 'Set':
#         print('setting temperature to ', values['-IN-'])
#         window['-TEMP OUT-'].update(values['-IN-'] + ' C')
#     elif event.startswith('Turn'):
#         print('Turning on the relay')
#     elif event == 'Off':
#         print('Turning off sensor')
#     elif event.startswith('F11'):
#         window.maximize()
#     elif event.startswith('Escape'):
#         window.normal()
#
#     window['-TEMP OUT-'].update(str(randint(2,70)) + ' C')

# import PySimpleGUI as sg
#
# """
#     Demo - Fill a listbox with list of files FilesBrowse button
#     This technique can be used to generate events from "Chooser Buttons" like FileBrowse, FilesBrowse
#     FolderBrowser, ColorChooserButton, Calendar Button
#     Any button that uses a "Target" can be used with an invisible Input Element to generate an
#     event when the user has made a choice.  Enable events for the invisible element and an event will
#     be generated when the Chooser Button fills in the element
#     This particular demo users a list of chosen files to populate a listbox
# """
#
#
# layout = [  [sg.LBox([], size=(20,10), key='-FILESLB-')],
#             [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
#             [sg.Button('Go'), sg.Button('Exit')]  ]
#
# window = sg.Window('Window Title', layout)
#
# while True:             # Event Loop
#     event, values = window.read()
#     if event in (None, 'Exit'):
#         break
#     # When choice has been made, then fill in the listbox with the choices
#     if event == '-IN-':
#         window['-FILESLB-'].Update(values['-IN-'].split(';'))
# window.close()

# import PySimpleGUI as sg
#
# sg.theme('BluePurple')
#
# layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]
#
# window = sg.Window('Pattern 2B', layout)
#
# while True:  # Event Loop
#     event, values = window.read()
#     print(event, values)
#     if event in  (None, 'Exit'):
#         break
#     if event == 'Show':
#         # Update the "output" text element to be the value of "input" element
#         window['-OUTPUT-'].update(values['-IN-'])
#
# window.close()