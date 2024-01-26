import tkinter as tk
from tkinter import ttk



class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        self.canvas = tk.Canvas(self, background='red')
        self.canvas.pack(expand=True, fill='both')

        # display frame
        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text='A label').pack()
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

# setup

window = tk.Tk()
window.geometry('500x400')
window.title('Scrolling Widgets')

text_list = [('label', 'button'), ('thing', 'click'), ('third', 'something'), ('label1', 'button'), ('label2', 'button2')]
list_frame = ListFrame(window, text_list, 100)
# run
window.mainloop()