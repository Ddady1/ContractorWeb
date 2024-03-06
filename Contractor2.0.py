import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import sqlite3

def get_col_names():
    try:
        conn = sqlite3.connect('contractor.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * from Contracts')
        col_names = list(map(lambda x: x[0], cursor.description))
        #print(col_names)
        return col_names

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()

def add_item(item_values):
    for item in item_values:
        if isinstance(item, tk.scrolledtext.ScrolledText) or isinstance(item, ttk.widgets.DateEntry):
            # now needs to make functions to get their data
            #print(type(item))
            pass
        else:
            print(item.get())
    col_names_list = get_col_names()
    col_names_list.pop(0)
    col_names = tuple(col_names_list)

    #print(type(col_names))
    print(col_names)
    try:
        conn = sqlite3.connect('contractor.db')
        cursor = conn.cursor()
        sqlite_insert_with_param = f'''INSERT INTO Contracts
                                    {col_names}
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
        cursor.execute(sqlite_insert_with_param, item_values)
        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()

def clear_fields(entries):
    for entry in entries:
        print(entry.cget('text'))
        entry.delete(0, 'end')

def display_item(item):
    print(item)

def get_data():
    conn = sqlite3.connect('contractor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from Contracts')
    raw_data = cursor.fetchall()
    #print(raw_data)
    col_names = list(map(lambda x: x[0], cursor.description))
    #print(col_names)
    display_tableview(col_names, raw_data)

def display_tableview(col_names, raw_data):
    def printsel(a):
        citem = dt.get_rows(selected=True)
        #print(citem[0].values)
        display_item(citem[0].values)
    coldata = []
    for name in col_names:
        col_dict = {'text': name, 'stretch': False}
        coldata.append(col_dict)



    '''coldata = [
        {"text": "LicenseNumber", "stretch": False},
        {'text': "CompanyName"},
        {"text": "UserCount", "stretch": False},
        {'text': 'Age', 'stretch': False}
    ]'''

    '''rowdata = [
        ('A123', 'IzzyCo', 12),
        ('A136', 'Kimdee Inc.', 45),
        ('A158', 'Farmadding Co.', 36),
        ('B432', 'sdfsfds', 45, 34)
    ]'''
    rowdata = raw_data

    dt = Tableview(
        master=data_frame,
        coldata=coldata,
        rowdata=rowdata,
        paginated=True,
        pagesize=40,
        searchable=True,
        bootstyle=PRIMARY,
        stripecolor=(None, None)
    )
    dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    dt.view.bind('<ButtonRelease-1>', printsel)


# Window
window = ttk.Window(themename='sandstone')
window.title('Contractor 1.0')
window.geometry('1200x800+250+100')
window.minsize(1200, 850)


# Frames

menu_frame = ttk.Frame(window)
data_frame = ttk.Frame(window, borderwidth=10, relief=SUNKEN)
item_frame = ttk.Frame(window, borderwidth=10, relief=SUNKEN)

# Frame layout

menu_frame.place(relx=0, rely=0, relwidth=1, relheight=0.05)
data_frame.place(relx=0, rely=0.05, relwidth=0.45, relheight=0.95)
item_frame.place(relx=0.45, rely=0.05, relwidth=0.55, relheight=0.95)



# Lebels for checkups
menu_label = ttk.Label(menu_frame, text='MENU', bootstyle=PRIMARY).pack(side='top', expand=True, fill='both')
#data_label = ttk.Label(data_frame, text='DATA', background='red').pack(side='left', expand=True, fill='both')
#item_label = ttk.Label(item_frame, text='ITEM', background='green').pack(side='left', expand=True, fill='both')

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
edit_menu.add_command(label='Add Item')
edit_menu.add_command(label='Edit Item')
edit_menu.add_separator()
edit_menu.add_command(label='Select All')


# Menubar Help

help_menu = ttk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')


# Create variables

product_name = ttk.StringVar()
manufacturer = ttk.StringVar()
supplier_name = ttk.StringVar()
start_date = ttk.StringVar()
exp_date = ttk.StringVar()
invoice_no = ttk.StringVar()
qty = ttk.StringVar()
invoice_date = ttk.StringVar()
lic_no = ttk.StringVar()
autho_no = ttk.StringVar()
contact_Fname = ttk.StringVar()
contact_Lname = ttk.StringVar()
contact_email = ttk.StringVar()
contact_mobile = ttk.StringVar()
remarks = ttk.StringVar()


# Item card label widgets
license_details_lb = ttk.Label(item_frame, text='License Details', bootstyle=PRIMARY, font=('Helvetica', 18, 'underline'))
product_name_lb = ttk.Label(item_frame, text='Product Name:', bootstyle=PRIMARY, font=('Helvetica', 12))
manufacturer_lb = ttk.Label(item_frame, text='Manufacturer:', bootstyle=PRIMARY, font=('Helvetica', 12))
supplier_name_lb = ttk.Label(item_frame, text='Supplier Name:', bootstyle=PRIMARY, font=('Helvetica', 12))
authorization_no_lb = ttk.Label(item_frame, text='Authorization No:', bootstyle=PRIMARY, font=('Helvetica', 12))
start_date_lb = ttk.Label(item_frame, text='Start Date:', bootstyle=PRIMARY, font=('Helvetica', 12))
exp_date_lb = ttk.Label(item_frame, text='Expiration Date:', bootstyle=PRIMARY, font=('Helvetica', 12))
invoice_no_lb = ttk.Label(item_frame, text='Invoice No:', bootstyle=PRIMARY, font=('Helvetica', 12))
invoice_date_lb = ttk.Label(item_frame, text='Invoice Date:', bootstyle=PRIMARY, font=('Helvetica', 12))
license_no_lb = ttk.Label(item_frame, text='License No:', bootstyle=PRIMARY, font=('Helvetica', 12))
quantity_lb = ttk.Label(item_frame, text='Quantity:', bootstyle=PRIMARY, font=('Helvetica', 12))
contact_details_lb = ttk.Label(item_frame, text='Contact Details', bootstyle=PRIMARY, font=('Helvetica', 18, 'underline'))
contact_fname_lb = ttk.Label(item_frame, text='First Name:', bootstyle=PRIMARY, font=('Helvetica', 12))
contact_lname_lb = ttk.Label(item_frame, text='Last Name:', bootstyle=PRIMARY, font=('Helvetica', 12))
contact_email_lb = ttk.Label(item_frame, text='Email:', bootstyle=PRIMARY, font=('Helvetica', 12))
contact_mobile_lb = ttk.Label(item_frame, text='Mobile:', bootstyle=PRIMARY, font=('Helvetica', 12))
remarks_lb = ttk.Label(item_frame, text='Remarks:', bootstyle=PRIMARY, font=('Helvetica', 12))


# item frame entry widgets
product_name_en = ttk.Entry(item_frame, textvariable=product_name)
manufacturer_en = ttk.Entry(item_frame, textvariable=manufacturer)
supplier_name_en = ttk.Entry(item_frame, textvariable=supplier_name)
authorization_no_en = ttk.Entry(item_frame, textvariable=autho_no)
start_date_en = ttk.DateEntry(item_frame, width=15, dateformat='%d/%m/%y')
exp_date_en = ttk.DateEntry(item_frame, width=15, dateformat='%d/%m/%y')
invoice_no_en = ttk.Entry(item_frame, textvariable=invoice_no)
invoice_date_en = ttk.DateEntry(item_frame, width=15, dateformat='%d/%m/%y')
license_no_en = ttk.Entry(item_frame, textvariable=lic_no)
quantity_en = ttk.Entry(item_frame, textvariable=qty)
contact_fname_en = ttk.Entry(item_frame, textvariable=contact_Fname)
contact_lname_en = ttk.Entry(item_frame, textvariable=contact_Lname)
contact_email_en = ttk.Entry(item_frame, textvariable=contact_email)
contact_mobile_en = ttk.Entry(item_frame, textvariable=contact_mobile)
remarks_en = ttk.ScrolledText(item_frame, width=71)
entry_list = [product_name_en, manufacturer_en, supplier_name_en, authorization_no_en, start_date_en, exp_date_en, invoice_no_en,
              invoice_date_en, license_no_en, quantity_en, contact_fname_en, contact_lname_en,
              contact_email_en, contact_mobile_en, remarks_en]

vars_list = (product_name, manufacturer, supplier_name, autho_no, start_date_en, exp_date_en, invoice_no, invoice_date_en,
             lic_no, qty, contact_Fname, contact_Lname, contact_email, contact_mobile, remarks_en)


#  item frame buttons widgets
add_bt = ttk.Button(item_frame, text='Add item', width=15, command=lambda: add_item(vars_list))
edit_bt = ttk.Button(item_frame, text='Edit item', width=15)
del_bt = ttk.Button(item_frame, text='Delete item', width=15)
clear_bt = ttk.Button(item_frame, text='Clear fields', width=15, command=lambda: clear_fields(entry_list))
exit_bt = ttk.Button(item_frame, text='Exit', width=15, bootstyle=DANGER, command=window.quit)


# item frame layout

item_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
item_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1, uniform='a')

# item frame label widgets layout

license_details_lb.grid(row=0, column=0, columnspan=5, sticky='n', padx=150)
product_name_lb.grid(row=1, column=0, sticky='w')
manufacturer_lb.grid(row=1, column=3, sticky='w')
supplier_name_lb.grid(row=2, column=0, sticky='w')
authorization_no_lb.grid(row=2, column=3, sticky='w')
start_date_lb.grid(row=3, column=0, sticky='w')
exp_date_lb.grid(row=3, column=3, sticky='w')
invoice_no_lb.grid(row=4, column=0, sticky='w')
invoice_date_lb.grid(row=4, column=3, sticky='w')
license_no_lb.grid(row=5, column=0, sticky='w')
quantity_lb.grid(row=5, column=3, sticky='w')
contact_details_lb.grid(row=6, column=0, columnspan=5, sticky='s', padx=150)
contact_fname_lb.grid(row=7, column=0, sticky='w')
contact_lname_lb.grid(row=7, column=3, sticky='w')
contact_email_lb.grid(row=8, column=0, sticky='w')
contact_mobile_lb.grid(row=8, column=3, sticky='w')
remarks_lb.grid(row=9, column=0, sticky='w')

# item frame entry widgets layout
product_name_en.grid(row=1, column=1, sticky='w')
manufacturer_en.grid(row=1, column=4, sticky='w')
supplier_name_en.grid(row=2, column=1, sticky='w')
authorization_no_en.grid(row=2, column=4, sticky='w')
start_date_en.grid(row=3, column=1, sticky='w')
exp_date_en.grid(row=3, column=4, sticky='w')
invoice_no_en.grid(row=4, column=1, sticky='w')
invoice_date_en.grid(row=4, column=4, sticky='w')
license_no_en.grid(row=5, column=1, sticky='w')
quantity_en.grid(row=5, column=4, sticky='w')
contact_fname_en.grid(row=7, column=1, sticky='w')
contact_lname_en.grid(row=7, column=4, sticky='w')
contact_email_en.grid(row=8, column=1, sticky='w')
contact_mobile_en.grid(row=8, column=4, sticky='w')
remarks_en.grid(row=9, column=1, columnspan=5, sticky='w')


# item frame buttons widgets layout
add_bt.grid(row=11, column=0, sticky='w')
edit_bt.grid(row=11, column=1, sticky='w')
del_bt.grid(row=11, column=2, sticky='w')
clear_bt.grid(row=11, column=3, sticky='w')
exit_bt.grid(row=11, column=4, sticky='w')






if __name__ == "__main__":
    get_data()
    #read_data()
    window.mainloop()