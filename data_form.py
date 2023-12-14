import tkinter as tk
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'


root = tk.Tk()
root.title('Data Form')
root.geometry('760x600+350+150')

#root.rowconfigure(2, weight=2)
product_lab = ttk.Label(root, text='Product:', foreground=text_color, font=('Ariel', 12, 'bold'))
product_ent = tk.Entry(root, width=30)
manuf_lab = ttk.Label(root, text='Manufacturer:', foreground=text_color, font=('Ariel', 12, 'bold'))
manuf_ent = tk.Entry(root, width=35)
qty_lab = ttk.Label(root, text='Quantity:', foreground=text_color, font=('Ariel', 12, 'bold'))
qty_ent = tk.Entry(root, width=10)


product_lab.grid(column=0, row=0, padx=5, pady=5)
product_ent.grid(column=1, row=0, columnspan=2)
manuf_lab.grid(column=3, row=0, padx=5, pady=5)
manuf_ent.grid(column=4, row=0, columnspan=2)
qty_lab.grid(column=6, row=0, padx=5, pady=5)
qty_ent.grid(column=7, row=0)




startDate_lab = ttk.Label(root, text='Start Date:', foreground=text_color, font=('Ariel', 12, 'bold'))
startDate_ent = tk.Entry(root, width=10)
expirationDate_lab = ttk.Label(root, text='Expiration Date:', foreground=text_color, font=('Ariel', 12, 'bold'))
expirationDate_ent = tk.Entry(root, width=10)
invoiceNo_lab = tk.Label(root, text="Invoice No':", foreground=text_color, font=('Ariel', 12, 'bold'))
invoiceNo_ent = tk.Entry(root, width=15)
invoiceDate_lab = tk.Label(root, text='Invoice Date:', foreground=text_color, font=('Ariel', 12, 'bold'))
invoiceDate_ent = tk.Entry(root, width=10)


'''startDate_lab.grid(column=0, row=2, padx=5, pady=5)
startDate_ent.grid(column=1, row=2)
expirationDate_lab.grid(column=2, row=2, padx=5, pady=5)
expirationDate_ent.grid(column=3, row=2)
invoiceNo_lab.grid(column=4, row=2, padx=5, pady=5, sticky=tk.W)
invoiceNo_ent.grid(column=5, row=2)
invoiceDate_lab.grid(column=6, row=2)
invoiceDate_ent.grid(column=7, row=2)'''

root.mainloop()

#if __name__ == '__main__':
