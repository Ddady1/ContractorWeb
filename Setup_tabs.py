import tkinter
import tkinter as tk
from tkinter import ttk
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('630x480+450+250')
root.resizable(False, False)

setup_notebook = ttkb.Notebook(root, bootstyle='light')
setup_notebook.pack(fill=X, pady=1, side=TOP)

info_tab = ttkb.Frame(setup_notebook, style='primary.TFrame')
db_sel_tab = ttkb.Frame(setup_notebook)

info_tab_lbl = ttkb.Label(info_tab, text='Welcome to Contractor setup', bootstyle='primary inverse', font=('Helvetica', 18))
info_tab_lbl.pack(side=TOP, fill=X, padx=10, pady=10)

#main_frame_lbl = ttkb.Frame(info_tab, bootstyle='primary')
#main_frame_lbl.pack(fill=BOTH)

info_lbl = ttkb.Label(info_tab, text='Contractor app was design to help you keep track of all your\n'
                                           'contracts and to manage that in one place.\n\n'
                                           'Contractor also will remind you when your contracts are about to\n'
                                           'be expired.\n\n'
                                           'Contractor is a Python base application and can work with various\n'
                                           'of databases such ad SQLite, MySQL, MongoDB and more...\n',
                      font=('Helvetica', 14), bootstyle='primary')
info_lbl.pack()
lbl = ttkb.Label(info_tab, bootstyle='primary inverse')
lbl.pack(fill=X)

cancel_btn = ttkb.Button(info_tab, text='Cancel', bootstyle='primary outline')
cancel_btn.pack()

setup_notebook.add(info_tab, text='Info')
setup_notebook.add(db_sel_tab, text='DB select')





root.mainloop()