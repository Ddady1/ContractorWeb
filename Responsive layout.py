import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self, start_size):
        super().__init__()
        self.title('Responsive layout')
        self.geometry(f'{start_size[0]}x{start_size[1]}')

        SizeNotifier(self, {300: self.create_small_layout, 600: self.create_medium_layout})

        self.mainloop()

    def create_small_layout(self):
        pass

    def create_medium_layout(self):
        pass

class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}

        self.window.bind('<Configure>', self.check_size)

    def check_size(self, event):
        print(event)



app = App((400, 300))
