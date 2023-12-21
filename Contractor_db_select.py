import tkinter as tk
from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
import os


def exit_app():

    result = Messagebox.show_question('Are you sure you want to cancel and exit the setup?', 'Cancel setup',
                                      buttons=['No:primary', 'Yes:danger'])
    if result == 'Yes':
        root.destroy()
def selected_database(selected):

    selected_db = selected
    print(selected_db)
    os.startfile('Contractor_SQLite_creation.py')



root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('600x450+450+250')
root.resizable(False, False)

headerbar_db = ttkb.Frame(style='primary.TFrame')
headerbar_db.pack(fill=X, pady=1, side=TOP)
wizard_db_lbl = ttkb.Label(headerbar_db, text='Choose your preferred Database', bootstyle='primary inverse', font=('Helvetica', 18))
wizard_db_lbl.pack(side=TOP, fill=X, padx=10, pady=10)

main_frame_lbl = ttkb.LabelFrame(root, text='Select Database', bootstyle='primary')
main_frame_lbl.place(x=10, y=80, width=580)

'''db_info_lbl = ttkb.Label(main_frame_lbl, text='Contractor can work with various Databases.\n\n'
                                           'Please choose your favourite Database:\n'
                                           , font=('Helvetica', 14), bootstyle='primary')
db_info_lbl.pack(side=LEFT, padx=10)'''

db_list = ['SQLite', 'MySQL', 'MongoDB', 'Excel File']
db_selection_var = StringVar()
i = 200
for db in db_list:
    ttkb.Radiobutton(main_frame_lbl, bootstyle='primary', variable=db_selection_var,
                     text=db, value=db).pack(pady=20, padx=20, fill=BOTH)

#sqlite_rb = ttk.Radiobutton(main_frame_lbl, bootstyle='primary', text='SQLite', value='d').pack(padx=20, pady=20, fill=BOTH)
#mysql_rb = ttk.Radiobutton(main_frame_lbl, bootstyle='primary', text='MySQL', value='s').pack(padx=20, pady=20, fill=BOTH)

db_cancel_btn = ttkb.Button(root, text='Cancel', command=exit_app)
db_cancel_btn.place(x=10, y=400, width=80)
db_prev_btn = ttkb.Button(root, text='Previous')
db_prev_btn.place(x=410, y=400, width=80)
db_next_btn = ttkb.Button(root, text='Next', command=lambda: selected_database(db_selection_var.get()))
db_next_btn.place(x=510, y=400, width=80)

root.mainloop()