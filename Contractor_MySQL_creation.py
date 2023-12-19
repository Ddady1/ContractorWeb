from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.dialogs import Messagebox
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

hostname = StringVar()
username = StringVar()
password = StringVar()

headerbar_db = ttkb.Frame(style='primary.TFrame')
headerbar_db.pack(fill=X, pady=1, side=TOP)
mysql_main_lbl = ttkb.Label(headerbar_db, text='MySQL database details', bootstyle='primary inverse', font=('Helvetica', 18))
mysql_main_lbl.pack(side=TOP, fill=X, padx=10, pady=10)


mysql_details_frame_lbl = ttkb.LabelFrame(root, text='Enter details', bootstyle='primary')
mysql_details_frame_lbl.place(x=10, y=80, width=580)

db_server_lbl = ttkb.Label(mysql_details_frame_lbl, text='Server address:', font=('Helvetica', 14), bootstyle='primary')
db_server_lbl.grid(column=0, row=0, padx=10, pady=20, sticky=W)

db_username_lbl = ttkb.Label(mysql_details_frame_lbl, text='DB user name:', font=('Helvetica', 14), bootstyle='primary')
db_username_lbl.grid(column=0, row=1, padx=10, pady=20, sticky=W)

db_password_lbl = ttkb.Label(mysql_details_frame_lbl, text='DB password:', font=('Helvetica', 14), bootstyle='primary')
db_password_lbl.grid(column=0, row=2, padx=10, pady=20, sticky=W)

db_server_ent = ttkb.Entry(mysql_details_frame_lbl, font=('Helvetica', 14), textvariable=hostname, width=35)
db_server_ent.grid(column=1, row=0, padx=5, pady=20, sticky=W)
db_server_ent.insert(0, r' Example: localhost or 192.168.1.1')
db_server_ent.bind("<Button-1>", lambda e: db_server_ent.delete(0, ttkb.END))

db_username_ent = ttkb.Entry(mysql_details_frame_lbl, font=('Helvetica', 14), textvariable=username, width=35)
db_username_ent.grid(column=1, row=1, padx=5, pady=20, sticky=W)
db_username_ent.insert(0, 'Please enter the DB username')
db_username_ent.bind("<Button-1>", lambda e: db_username_ent.delete(0, ttkb.END))

db_password_ent = ttkb.Entry(mysql_details_frame_lbl, font=('Helvetica', 14), textvariable=password, width=35)
db_password_ent.grid(column=1, row=2, padx=5, pady=20, sticky=W)
db_password_ent.insert(0, 'Please enter the DB password')
db_password_ent.bind("<Button-1>", lambda e: db_password_ent.delete(0, ttkb.END))




db_cancel_btn = ttkb.Button(root, text='Cancel', command=exit_app)
db_cancel_btn.place(x=10, y=400, width=80)
db_prev_btn = ttkb.Button(root, text='Previous')
db_prev_btn.place(x=410, y=400, width=80)
db_next_btn = ttkb.Button(root, text='Next')
db_next_btn.place(x=510, y=400, width=80)

root.mainloop()