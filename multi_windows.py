import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

class Extra(ttk.Toplevel):
    def __init__(self):
        super(Extra, self).__init__()
        self.title('Extra Window')
        self.geometry('300x400')
        ttk.Label(self, text='A Label').pack()
        ttk.Button(self, text='A Button').pack()
        ttk.Label(self, text='Another label').pack(expand=True)
def ask_yes_no():
    messagebox.askquestion('Title', 'Body')

def create_window():
    global extra_window
    extra_window = Extra()
    #extra_window = ttk.Toplevel()
    #extra_window.title('Extra Window')
    #extra_window.geometry('300x400')
    #ttk.Label(extra_window, text='A Label').pack()
    #ttk.Button(extra_window, text='A Button').pack()
    #ttk.Label(extra_window, text='Another label').pack(expand=True)

def close_window():
    extra_window.destroy()

# window
window = ttk.Window()
window.geometry('600x400')
window.title('Multiple windows')

button1 = ttk.Button(window, text='open main window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='close main window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(window, text='create yes no window', command=ask_yes_no)
button3.pack(expand=True)

#run
window.mainloop()
