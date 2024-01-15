import tkinter
import tkinter as tk
from tkinter import ttk
from ttkbootstrap.dialogs import Messagebox
from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

def main_dis():
    main_frame.destroy()

def exit_app():
    result = Messagebox.show_question('Are you sure you want to cancel and exit the setup?', 'Cancel setup',
                                      buttons=['No:primary', 'Yes:danger'])
    if result == 'Yes':
        root.destroy()



def setup_next():
    global count

    if not count > len(frames) - 2:
        for frame in frames:
            frame.pack_forget()

        count += 1
        if count == 2:
            print(db_selection_var.get())
        frame = frames[count]
        frame.pack(pady=50, padx=20, fill=X)






def setup_prev():
    global count

    if not count == 0:
        for frame in frames:
            frame.pack_forget()

        count -= 1
        frame = frames[count]
        frame.pack(pady=50, padx=20, fill=X)


def auto_db_gauge():
    global process
    process += 2
    db_build_gauge['value'] = process
    if db_build_gauge['value'] >= 100:
        db_build_gauge['mask'] = 'Database was created successfully'
        auto_tb_gauge()
        return
    root.after(100, auto_db_gauge)


def auto_tb_gauge():
    global process1
    process1 += 2
    tables['value'] = process1
    if tables['value'] >= 100:
        tables['mask'] = 'Tables were created successfully'
        return
    root.after(100, auto_tb_gauge)





'''def info_frame():

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
    sqlite_set_lf = ttkb.Label(main_frame, text='Creating SQlite database', bootstyle='primary')

    sqlite_set_lf.pack()'''


root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('630x480+450+250')
root.resizable(False, False)

# Main Frame contaiuner

main_frame = ttkb.Frame(root)

# Frame 1

setup_info_lf = ttkb.LabelFrame(main_frame, text='About', bootstyle='primary')
'''setup_top_lbl = ttkb.Label(main_frame, text='  Welcome to Contractor setup', bootstyle='primary inverse',
                               font=('Helvetica', 20))
setup_top_lbl.pack(side=TOP, fill=X, padx=2, pady=1, ipady=10)'''
setup_info_lbl = ttkb.Label(setup_info_lf, text='Contractor app was design to help you keep track of all your\n'
                                                    'contracts and to manage that in one place.\n\n'
                                                    'Contractor also will remind you when your contracts are about to\n'
                                                    'be expired.\n\n'
                                                    'Contractor is a Python base application and can work with various\n'
                                                    'of databases such ad SQLite, MySQL, MongoDB and more...\n',
                                font=('Helvetica', 15), bootstyle='primary')
setup_info_lbl.pack()
setup_info_lf.pack(pady=50)

# Frame 2

db_select_lf = ttkb.LabelFrame(main_frame, text='Select Database', bootstyle='primary')
'''db_select_top_lbl = ttkb.Label(main_frame, text='  Choose your preferred Database', bootstyle='primary inverse',
                               font=('Helvetica', 20))
db_select_top_lbl.pack(side=TOP, fill=X, padx=2, pady=1, ipady=10)'''
db_list = ['SQLite', 'MySQL', 'MongoDB', 'Excel File']
db_selection_var = StringVar()
i = 200
for db in db_list:
    ttkb.Radiobutton(db_select_lf, bootstyle='primary', variable=db_selection_var,
                        text=db, value=db).pack(pady=20, padx=20, fill=BOTH)

# Frame 3

sqlite_set_lf = ttkb.LabelFrame(main_frame, text='Creating SQlite database', bootstyle='primary')

db_build_gauge = ttkb.Floodgauge(sqlite_set_lf, bootstyle='', maximum=100,
                                 mask='Building database: {}%', font=('Helvetica', 18))
db_build_gauge.pack(pady=20, fill=X, padx=20)

tables = ttkb.Floodgauge(sqlite_set_lf, maximum=100, mask='Building tables: {}%', font=('Helvetica', 18))
tables.pack(pady=20, fill=X, padx=20)
process = 0
auto_db_gauge()
process1 = 0


# Frame 4

main_frame.pack(pady=1, fill=BOTH, expand=True)


frames = [setup_info_lf, db_select_lf, sqlite_set_lf]
count = 0

bottom_frame = ttkb.Frame(root)

cancel_btn = ttkb.Button(bottom_frame, text='Cancel', width=8, command=exit_app)
cancel_btn.pack(side=ttkb.LEFT, padx=20, pady=5)

next_btn = ttkb.Button(bottom_frame, text='Next', width=8, command=setup_next)
next_btn.pack(side=ttkb.RIGHT, padx=20, pady=5)

prev_btn = ttkb.Button(bottom_frame, text='Previous', width=8, command=setup_prev)
prev_btn.pack(side=ttkb.RIGHT, padx=10, pady=5)


bottom_frame.pack(side=ttkb.BOTTOM, pady=10, fill=X)


root.mainloop()