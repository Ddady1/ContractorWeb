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

db_server_ent = ttkb.Entry(mysql_details_frame_lbl, font=('Helvetica', 14), textvariable=hostname)
db_server_ent.pack(padx=20, pady=20)


db_cancel_btn = ttkb.Button(root, text='Cancel', command=exit_app)
db_cancel_btn.place(x=10, y=400, width=80)
db_prev_btn = ttkb.Button(root, text='Previous')
db_prev_btn.place(x=410, y=400, width=80)
db_next_btn = ttkb.Button(root, text='Next')
db_next_btn.place(x=510, y=400, width=80)

root.mainloop()