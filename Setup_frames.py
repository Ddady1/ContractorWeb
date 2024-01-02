import tkinter
import tkinter as tk
from tkinter import ttk
from ttkbootstrap.dialogs import Messagebox
from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

def main_dis():
    main_frame.destroy()


def setup_next(frames_list):
    global count





    pass





def setup_prev():
    pass




def info_frame():

    setup_info_lf = ttkb.LabelFrame(main_frame, text='About', bootstyle='primary')
    setup_top_lbl = ttkb.Label(main_frame, text='  Welcome to Contractor setup', bootstyle='primary inverse',
                               font=('Helvetica', 20))
    setup_top_lbl.pack(side=TOP, fill=X, padx=2, pady=1, ipady=10)
    setup_info_lbl = ttkb.Label(setup_info_lf, text='Contractor app was design to help you keep track of all your\n'
                                                    'contracts and to manage that in one place.\n\n'
                                                    'Contractor also will remind you when your contracts are about to\n'
                                                    'be expired.\n\n'
                                                    'Contractor is a Python base application and can work with various\n'
                                                    'of databases such ad SQLite, MySQL, MongoDB and more...\n',
                                font=('Helvetica', 15), bootstyle='primary')
    setup_info_lbl.pack()
    setup_info_lf.pack(pady=50)



def db_select_frame():

    db_select_lf = ttkb.LabelFrame(main_frame, text='Select Database', bootstyle='primary')
    db_select_top_lbl = ttkb.Label(main_frame, text='  Choose your preferred Database', bootstyle='primary inverse',
                               font=('Helvetica', 20))
    db_select_top_lbl.pack(side=TOP, fill=X, padx=2, pady=1, ipady=10)
    db_list = ['SQLite', 'MySQL', 'MongoDB', 'Excel File']
    db_selection_var = StringVar()
    i = 200
    for db in db_list:
        ttkb.Radiobutton(db_select_lf, bootstyle='primary', variable=db_selection_var,
                         text=db, value=db).pack(pady=20, padx=20, fill=BOTH)
    db_select_lf.pack(padx=20, pady=50, fill=X)



def sqlite_frame():
    pass


root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('630x480+450+250')
root.resizable(False, False)

main_frame = ttkb.Frame(root)

frames = (info_frame, db_select_frame, sqlite_frame)
count = 0



'''setup_info_lf = ttkb.LabelFrame(main_frame, text='About', bootstyle='primary')
setup_top_lbl = ttkb.Label(main_frame, text='  Welcome to Contractor setup', bootstyle='primary inverse', font=('Helvetica', 20))
setup_top_lbl.pack(side=TOP, fill=X, padx=2, pady=1, ipady=10)
setup_info_lbl = ttkb.Label(setup_info_lf, text='Contractor app was design to help you keep track of all your\n'
                                           'contracts and to manage that in one place.\n\n'
                                           'Contractor also will remind you when your contracts are about to\n'
                                           'be expired.\n\n'
                                           'Contractor is a Python base application and can work with various\n'
                                           'of databases such ad SQLite, MySQL, MongoDB and more...\n',
                      font=('Helvetica', 15), bootstyle='primary')
setup_info_lbl.pack()
setup_info_lf.pack(pady=50)'''

main_frame.pack(pady=1, fill=BOTH, expand=True)



bottom_frame = ttkb.Frame(root)

cancel_btn = ttkb.Button(bottom_frame, text='Cancel', width=8, command=main_dis)
cancel_btn.pack(side=ttkb.LEFT, padx=20, pady=5)

next_btn = ttkb.Button(bottom_frame, text='Next', width=8, command=lambda: setup_next(frames))
next_btn.pack(side=ttkb.RIGHT, padx=20, pady=5)

prev_btn = ttkb.Button(bottom_frame, text='Previous', width=8, command=setup_prev())
prev_btn.pack(side=ttkb.RIGHT, padx=10, pady=5)



bottom_frame.pack(side=ttkb.BOTTOM, pady=10, fill=X)



#info_frame()



root.mainloop()