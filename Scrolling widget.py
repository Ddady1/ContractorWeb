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
        self.canvas = tk.Canvas(self, background='red', scrollregion=(0, 0, 500, self.list_height))
        self.canvas.pack(expand=True, fill='both')

        # display frame
        self.frame = ttk.Frame(self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item)

        self.canvas.create_window((0, 0), window=self.frame, anchor='nw', width=500, height=self.list_height)

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        # grid layout
        frame.rowconfigure(0, window=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        # widgets
        ttk.Label(frame, text=f'#{index}')

# setup

window = tk.Tk()
window.geometry('500x400')
window.title('Scrolling Widgets')

text_list = [('label', 'button'), ('thing', 'click'), ('third', 'something'), ('label1', 'button'), ('label2', 'button2')]
list_frame = ListFrame(window, text_list, 100)
# run
window.mainloop()