import tkinter as tk
from tkinter import ttk
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


def exit_app():
    result = Messagebox.show_question('Are you sure you want to cancel and exit the setup?', 'Cancel setup',
                                      buttons=['No:primary', 'Yes:danger'])
    if result == 'Yes':
        root.destroy()


root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('600x450+450+250')
root.resizable(False, False)

headerbar = ttkb.Frame(style='primary.TFrame')
headerbar.pack(fill=X, pady=1, side=TOP)
wizard_1_lbl = ttkb.Label(headerbar, text='Welcome to Contractor setup', bootstyle='primary inverse', font=('Helvetica', 18))
wizard_1_lbl.pack(side=TOP, fill=X, padx=10, pady=10)

main_frame_lbl = ttkb.LabelFrame(root, text='About', bootstyle='primary')
main_frame_lbl.place(x=10, y=100, width=580)

info_lbl = ttkb.Label(main_frame_lbl, text='Contractor app was design to help you keep track of all your\n'
                                           'contracts and to manage that in one place.\n\n'
                                           'Contractor also will remind you when your contracts are about to\n'
                                           'be expired.\n\n'
                                           'Contractor is a Python base application and can work with various\n'
                                           'of databases such ad SQLite, MySQL, MongoDB and more...\n',
                      font=('Helvetica', 14), bootstyle='primary')
info_lbl.pack(padx=10, pady=10)

'''footerbar = ttkb.Frame(root, style='primary.TFrame')
footerbar.place(x=0, y=350)
footer_lbl = ttkb.Label(footerbar, text='--------------------------------------------------------------------------', bootstyle='primary inverse', font=('Helvetica', 18))
footer_lbl.pack()'''

cancel_btn = ttkb.Button(root, text='Cancel', command=exit_app)
cancel_btn.place(x=400, y=400, width=80)

next_btn = ttkb.Button(root, text='Next')
next_btn.place(x=500, y=400, width=80)




root.mainloop()