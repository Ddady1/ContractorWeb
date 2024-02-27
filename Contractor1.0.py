import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

def read_data():

    coldata = [
        {"text": "LicenseNumber", "stretch": False},
        "CompanyName",
        {"text": "UserCount", "stretch": False},
    ]

    rowdata = [
        ('A123', 'IzzyCo', 12),
        ('A136', 'Kimdee Inc.', 45),
        ('A158', 'Farmadding Co.', 36)
    ]

    dt = Tableview(
        master=data_frame,
        coldata=coldata,
        rowdata=rowdata,
        paginated=True,
        searchable=True,
        bootstyle=PRIMARY,
        stripecolor=(None, None),
    )
    dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)


# Window
window = ttk.Window(themename='sandstone')
window.geometry('1300x800+250+100')
window.title('Contractor 1.0')
window.geometry('1200x800+250+100')


# Frames

menu_frame = ttk.Frame(window)
data_frame = ttk.Frame(window)
item_frame = ttk.Frame(window)

# Frame layout

menu_frame.place(relx=0, rely=0, relwidth=1, relheight=0.05)
data_frame.place(relx=0, rely=0.05, relwidth=0.5, relheight=0.95)
item_frame.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.95)


# Lebels for checkups
menu_label = ttk.Label(menu_frame, text='MENU', background='blue').pack(side='top', expand=True, fill='both')
#data_label = ttk.Label(data_frame, text='DATA', background='red').pack(side='left', expand=True, fill='both')
item_label = ttk.Label(item_frame, text='ITEM', background='green').pack(side='left', expand=True, fill='both')

# Menubar

menu_bar = ttk.Menu(menu_frame)
window.config(menu=menu_bar)

# Menubar File menu

file_menu = ttk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open...')
file_menu.add_separator()
file_menu.add_command(label='Print')
file_menu.add_separator()

# Menubar File->export submenu

export_submenu = ttk.Menu(file_menu, tearoff=False)
export_submenu.add_command(label='to CSV')
export_submenu.add_command(label='to Excel')
export_submenu.add_command(label='to PDF')
file_menu.add_cascade(label='Export...', menu=export_submenu)


# Menubar File->import submenu
import_submenu = ttk.Menu(file_menu, tearoff=False)
import_submenu.add_command(label='from CSV')
import_submenu.add_command(label='from Excel')
#import_submenu.add_command(label='to PDF')
file_menu.add_cascade(label='Import...', menu=import_submenu)


# Menubar File->exit

file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.quit)


# Menubar Edit

edit_menu = ttk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Add Contract')
edit_menu.add_command(label='Edit Contract')
edit_menu.add_separator()
edit_menu.add_command(label='Select All')


if __name__ == "__main__":
    read_data()
    window.mainloop()