import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Place')
'''window.title('Pack')'''
window.geometry('400x600')

#window.title('Grid')
#window.geometry('600x400')



'''# widgets
label1 = ttk.Label(window, text = 'First label', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Last of the labels', background = 'green')
button = ttk.Button(window, text = 'Button')

label1.pack(side='top', expand=True, fill='both', pady=10, padx=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')'''

label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Label 3', background='green')
label4 = ttk.Label(window, text='Label 4', background='yellow')
button1 = ttk.Button(window, text='Button 1')
button2 = ttk.Button(window, text='Button 2')
entry = ttk.Entry(window)

label1 = ttk.Label(window, text='Lable 1', background='red')
label2 = ttk.Label(window, text='Lable 2', background='blue')
label3 = ttk.Label(window, text='Lable 3', background='green')
button1 = ttk.Button(window, text='Raise lebel 1', command=lambda: label1.tkraise(aboveThis=label2))
button2 = ttk.Button(window, text='Raise label 2', command=lambda: label2.tkraise())
button3 = ttk.Button(window, text='Raise lebel 3', command=lambda: label3.tkraise())


'''# Layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=80, y=60, width=160, height=300)
button1.place(relx=0.6, rely=1, anchor='se')
button2.place(relx=0.8, rely=1, anchor='se')
button3.place(relx=1, rely=1, anchor='se')'''


'''# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text='Frame label', background='yellow')
frame_button = ttk.Button(frame, text='Frame button')

# frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)'''


'''# define a grid
window.columnconfigure((0, 1, 2), weight=1, uniform='a')
#window.columnconfigure(1, weight=1)
#window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=2, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')

# place a widget
label1.grid(row=0, column=0, sticky='nsew')
label2.grid(row=1, column=1, rowspan=3, sticky='nsew')
label3.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=20, pady=10)
label4.grid(row=3, column=3, sticky='se')
button1.grid(row=0, column=3, sticky='nsew')
button2.grid(row=2, column=2, sticky='nsew')
entry.grid(row=2, column=3, rowspan=2)'''



window.mainloop()