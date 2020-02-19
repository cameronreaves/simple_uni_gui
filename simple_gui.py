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


# import PySimpleGUI as sg
# #
# # frame_layout = [
# #                   [sg.T('Text inside of a frame')],
# #                   [sg.CB('Check 1'), sg.CB('Check 2')],
# #                ]
# # layout = [
# #           [sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='blue')],
# #           [sg.Submit(), sg.Cancel()]
# #          ]
# #
# # window = sg.Window('Frame with buttons', layout, font=("Helvetica", 12))
# #
# # window.read()



# TABS
# layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
#               [sg.Button('Read')]]

