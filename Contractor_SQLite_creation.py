import tkinter as tk
from tkinter import ttk
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import time

def exit_app():
    result = Messagebox.show_question('Are you sure you want to cancel and exit the setup?', 'Cancel setup',
                                      buttons=['No:primary', 'Yes:danger'])
    if result == 'Yes':
        root.destroy()


def auto():
    pass


root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('600x450+450+250')
root.resizable(False, False)


headerbar_lite = ttkb.Frame(style='primary.TFrame')
headerbar_lite.pack(fill=X, pady=1, side=TOP)
main_lite_lbl = ttkb.Label(headerbar_lite, text='SQLite database creation', bootstyle='primary inverse', font=('Helvetica', 18))
main_lite_lbl.pack(side=TOP, fill=X, padx=10, pady=10)


lite_frame_lbl = ttkb.LabelFrame(root, text='SQLite database setup', bootstyle='primary')
lite_frame_lbl.place(x=10, y=80, width=580)

db_build_progress = ttkb.Progressbar(lite_frame_lbl, bootstyle='primary striped', maximum=100, value=0)
db_build_progress.pack(pady=10, padx=10, fill=X)
auto()







lite_cancel_btn = ttkb.Button(root, text='Cancel', command=exit_app)
lite_cancel_btn.place(x=10, y=400, width=80)
lite_prev_btn = ttkb.Button(root, text='Previous')
lite_prev_btn.place(x=410, y=400, width=80)
lite_next_btn = ttkb.Button(root, text='Finish')
lite_next_btn.place(x=510, y=400, width=80)


root.mainloop()