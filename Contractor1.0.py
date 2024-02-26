import tkinter as tk
import ttkbootstrap as ttk


# Window
window = ttk.Window(themename='sandstone')
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
data_label = ttk.Label(data_frame, text='DATA', background='red').pack(side='left', expand=True, fill='both')
item_label = ttk.Label(item_frame, text='ITEM', background='green').pack(side='left', expand=True, fill='both')

# Menubar

menu_bar = ttk.Menu(menu_frame)
window.config(menu=menu_bar)

# Menubar File menu

file_menu = ttk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New...')
file_menu.add_separator()
file_menu.add_command(label='Print')
file_menu.add_separator()

# Menubar export submenu

export_submenu = ttk.Menu(file_menu, tearoff=False)
export_submenu.add_command(label='to CSV')
export_submenu.add_command(label='to Excel')
export_submenu.add_command(label='to PDF')
file_menu.add_cascade(label='Export...', menu=export_submenu)


# Menubar import submenu
import_submenu = ttk.Menu(file_menu, tearoff=False)
import_submenu.add_command(label='from CSV')
import_submenu.add_command(label='from Excel')
#import_submenu.add_command(label='to PDF')
file_menu.add_cascade(label='Import...', menu=import_submenu)


# Menubar exit

file_menu.add_separator()
file_menu.add_command(label='Exit')


window.mainloop()