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

menu_frame.place(relx=0, rely=0, relheight=0.1, relwidth=1)
data_frame.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.9)
item_frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)




window.mainloop()