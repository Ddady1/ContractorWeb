import ttkbootstrap as ttk
import tkinter as tk
from random import randint, choice

window = ttk.Window()
window.geometry('600x400')
window.title('Scrolling')

'''### canvas ###
canvas = ttk.Canvas(window, background='white', scrollregion=(0, 0, 2000, 5000))
canvas.create_line(0, 0, 2000, 5000, fill='blue', width=10)
for i in range(100):
    l = randint(0, 2000)
    t = randint(0, 5000)
    r = l + randint(10, 500)
    b = t + randint(10, 500)
    color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
    canvas.create_rectangle(l, t, r, b, fill=color)
canvas.pack(expand=True, fill='both')

# mosuewhell scrolling
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), 'units'))

# mousewheel and CTRL
canvas.bind('<Control-MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), 'units'))

# scrollbar-Y
scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

# scrollbar X
scrollbarx = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbarx.set)
scrollbarx.place(relx=0, rely=1, relwidth=1, anchor='sw')'''

#### Text box ###

'''text = ttk.Text(window)
for i in range(1, 200):
    text.insert(f'{1}.0', f'text: {i} \n')
text.pack(expand=True, fill='both')

scrollbar_text = ttk.Scrollbar(window, orient='vertical', command=text.yview)
text.configure(yscrollcommand=scrollbar_text.set)
scrollbar_text.place(relx=1, rely=0, relheight=1, anchor='ne')'''

#### treeview ###
table = ttk.Treeview(window, columns=(1, 2), show='headings')
table.heading(1, text='First Name')
table.heading(2, text='Last Name')
first_names = ['Bob', 'Maria', 'David', 'Maya', 'Ron', 'Alex', 'Judy']
last_names = ['Racha', 'Jhon', 'Tels', 'yosd', 'dfer','werew', 'ergfer']
for i in range(100):
    table.insert(parent='', index=ttk.END, values=(choice(first_names), choice(last_names)))
table.pack(expand=True, fill='both')

scrollbar_table = ttk.Scrollbar(window, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor='ne')

window.mainloop()