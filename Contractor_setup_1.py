import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('600x450+450+250')

buttonbar = ttk.Frame(style='primary.TFrame')
buttonbar.pack(fill=X, pady=1, side=TOP)
wizard_1_lbl = ttkb.Label(buttonbar, text='Welcome to Contractor setup', bootstyle='primary inverse', font=('Helvetica', 18))
wizard_1_lbl.pack(side=TOP, fill=X, padx=10, pady=10)

main_frame_lbl = ttkb.LabelFrame(root, text='About', bootstyle='primary')
main_frame_lbl.place(x=10, y=60, width=580)

info_lbl = ttkb.Label(main_frame_lbl, text='', font=('Helvetica', 14), bootstyle='primary')
info_lbl.pack(padx=10, pady=10)

cancel_btn = ttkb.Button(root, text='Cancel', bootstyle='primary')
cancel_btn.place(x=500, y=400)




root.mainloop()