import tkinter
import tkinter as tk
from tkinter import ttk
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


root = ttkb.Window(themename='sandstone')
#root = tk.Tk()
root.title('Contractor Wizard')
root.geometry('630x480+450+250')
root.resizable(False, False)


bottom_frame = ttkb.Frame(root)

cancel_btn = ttkb.Button(bottom_frame, text='Cancel', width=8)
cancel_btn.pack(side=ttkb.LEFT, padx=20, pady=5)

next_btn = ttkb.Button(bottom_frame, text='Next', width=8)
next_btn.pack(side=ttkb.RIGHT, padx=20, pady=5)

prev_btn = ttkb.Button(bottom_frame, text='Previous', width=8)
prev_btn.pack(side=ttkb.RIGHT, padx=10, pady=5)



bottom_frame.pack(side=ttkb.BOTTOM, pady=10, fill=X)







root.mainloop()