import tkinter as tk
import ttkbootstrap as ttk
#from tkinter import ttk


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, exercise_text):
        super().__init__(master=parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
        self.create_exercise_box(exercise_text).grid(row=0, column=2, sticky='nsew')
        self.pack(expand=True, fill='both', padx=10, pady=10)

    def create_exercise_box(self, text):
        frame = ttk.Frame(master=self)
        ttk.Entry(frame).pack(expand=True, fill='both', padx=5, pady=5)
        ttk.Button(frame, text=text).pack(expand=True, fill='both', padx=5)

        return frame

# window
window = ttk.Window(themename='sandstone')
window.title('Widgets and return')
window.geometry('400x600')
window.minsize(400, 600)
# widgets
Segment(window, 'label', 'button', 'test')
Segment(window, 'test', 'click', 'something')
Segment(window, 'hello', 'test', 'other')
Segment(window, 'bye', 'launch', 'exit')
Segment(window, 'last one', 'exit', 'end')


# run
window.mainloop()