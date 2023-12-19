from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


def exit_app():
    result = Messagebox.show_question('Are you sure you want to cancel and exit the setup?', 'Cancel setup',
                                      buttons=['No:primary', 'Yes:danger'])
    if result == 'Yes':
        root.destroy()


def auto_db_gauge():
    global process
    process += 2
    db_build_gauge['value'] = process
    if db_build_gauge['value'] >= 100:
        db_build_gauge['mask'] = 'Database was created successfully'
        auto_tb_gauge()
        return
    root.after(100, auto_db_gauge)


def auto_tb_gauge():
    global process1
    process1 += 2
    tables['value'] = process1
    if tables['value'] >= 100:
        tables['mask'] = 'Tables were created successfully'
        return
    root.after(100, auto_tb_gauge)


def auto_db_con_gauge():
    global process2
    process2 += 2
    db_connect_gauge['value'] = process2
    if db_connect_gauge['value'] >= 100:
        db_connect_gauge['mask'] = 'Connection was established successfully'
        auto_db_gauge()
        return
    root.after(100, auto_db_con_gauge)


root = ttkb.Window(themename='sandstone')
root.title('Contractor Wizard')
root.geometry('600x450+450+250')
root.resizable(False, False)


headerbar_lite = ttkb.Frame(style='primary.TFrame')
headerbar_lite.pack(fill=X, pady=1, side=TOP)
main_lite_lbl = ttkb.Label(headerbar_lite, text='MySQL database creation', bootstyle='primary inverse', font=('Helvetica', 18))
main_lite_lbl.pack(side=TOP, fill=X, padx=10, pady=10)


lite_frame_lbl = ttkb.LabelFrame(root, text='MySQL database setup', bootstyle='primary')
lite_frame_lbl.place(x=10, y=80, width=580)

db_connect_gauge = ttkb.Floodgauge(lite_frame_lbl, bootstyle='', maximum=100, mask='Connecting to DB: {}%', font=('Helvetica', 18))
db_connect_gauge.pack(pady=20, fill=X, padx=20)

db_build_gauge = ttkb.Floodgauge(lite_frame_lbl,bootstyle='secondary', maximum=100, mask='Building database: {}%', font=('Helvetica', 18))
db_build_gauge.pack(pady=20, fill=X, padx=20)

tables = ttkb.Floodgauge(lite_frame_lbl, maximum=100, mask='Building tables: {}%', font=('Helvetica', 18))
tables.pack(pady=20, fill=X, padx=20)
process2 = 0
auto_db_con_gauge()
process = 0
#auto_db_gauge()
process1 = 0
#auto_tb_gauge()


lite_cancel_btn = ttkb.Button(root, text='Cancel', command=exit_app)
lite_cancel_btn.place(x=10, y=400, width=80)
lite_prev_btn = ttkb.Button(root, text='Previous')
lite_prev_btn.place(x=410, y=400, width=80)
lite_next_btn = ttkb.Button(root, text='Finish')
lite_next_btn.place(x=510, y=400, width=80)

root.mainloop()
