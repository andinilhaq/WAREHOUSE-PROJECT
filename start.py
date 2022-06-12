from csv import excel
import PySimpleGUI as ui
import pandas as pd
import openpyxl as xl
from openpyxl import workbook

ui.theme('DarkBlue2')
file_excel = 'Pendataan.xlsx'

rd = pd.read_excel(file_excel)

layout=[
[ui.Text('Program Pencatatan Warehouse', size=(25,2))],
[ui.Text('Transaction Type',size=(20,1)),ui.Combo(['ADD_STOCK','BUY_ITEM'],key='Tipe')],
[ui.Text('Item',size=(20,1)),ui.Combo(['Ballpoint', 'Buku Tulis', 'Pensil', 'Penggaris', 'Correction Tape'],key='Item')],
[ui.Text('Stock Change',size=(20,1)),ui.InputText(key='Perubahan stok')],
[ui.Text('Harga',size=(20,1)),ui.InputText(key='Pendapatan')],
[ui.Button('Submit'),ui.Button('Clear'),ui.Button('Format'), ui.Button('Exit')]
]

window=ui.Window('Warehouse App',layout)

def clear_input():
    for key in values:
        window[key]('')
        return None

def format():
    layout=[
    [ui.Text('Apakah anda yakin ingin memformat data?',key='new')],
    [ui.Button('Ya'), ui.Button('Tidak')]
    ]
    window = ui.Window('Format Window', layout, modal=True)
    choice=None

    while True:
        event, values = window.read()
        if event == 'Ya':
            file_excel = 'Pendataan.xlsx'
            book = xl.load_workbook(file_excel)
            sheet = book['Sheet1']
            sheet.delete_rows(2, sheet.max_row-1)
            ui.popup('Format Success')
            clear_input()
        if event == 'Tidak' or event == ui.WIN_CLOSED:
            break
    window.close

while True:
    event, values = window.read()
    if event == ui.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Format':
        format()
    if event == 'Submit':
        rd = rd.append(values, ignore_index=True)
        rd.to_excel(file_excel, index=False)
        ui.popup('Data Updated!')
        clear_input()
window.close()