import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Form')
root.geometry('800x600+350+150')

root.rowconfigure(0, weight=2)
name_lb = tk.Label(root, text='Product:')
name_en = tk.Entry(root)
manuf_lb = tk.Label(root, text='Manufacturer:')
manuf_en = tk.Entry(root, width=50)
qty_lb = tk.Label(root, text='Quantity:')
qty_en = tk.Entry(root)


name_lb.grid(column=0, row=0, padx=5, pady=5, sticky=tk.N)
name_en.grid(column=1, row=0, padx=5, pady=5)
manuf_lb.grid(column=2, row=0, padx=5, pady=5)
manuf_en.grid(column=3, row=0, padx=5, pady=5)
qty_lb.grid(column=4, row=0, padx=5, pady=5)
qty_en.grid(column=5, row=0, padx=5, pady=5)


root.mainloop()