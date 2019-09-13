import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Adder(ttk.Frame):
    """The adders gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        """Exits program."""
        tk.quit()

    def calculate(self, *args):
        """Calculates the sum of the two inputted numbers."""
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())
        num3 = round(((num1 * num2)/1000000), 6)
        num4 = round((num3 * 10), 6)
        num5 = round((num3 * 100), 6)
        self.answer_label['text'] = num3
        self.answer_label2['text'] = num4
        self.answer_label3['text'] = num5

        
    def init_gui(self):
        self.root.title('PPM Calculator')
        self.root.option_add('*tearOff', 'FALSE')

        self.grid(column=0, row=0, sticky='nsew')
        # Menu bar
        self.menubar = tk.Menu(self.root)

        def on_quit():
            exit()

        def hello():
            self.msg = tk.messagebox.showinfo("Info", "Hello")
            self.msg = tk.messagebox.showerror("Error", "Error")
            self.msg = tk.messagebox.showwarning("Warning", "Hello")
            self.msg = tk.messagebox.askquestion("Question", "How are you?")
            self.msg = tk.messagebox.askokcancel("Cancel", "Would You like to cancel")
            self.msg = tk.messagebox.askyesno("yesno", "yes? no?")
            self.msg = tk.messagebox.askretrycancel("retry", "cancel?")
            

        
        self.menu_file = tk.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=on_quit)
        
        self.menu_edit = tk.Menu(self.menubar)
        self.menu_edit.add_command(label='Hello', command=hello)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

        self.num1_entry = ttk.Entry(self, width=5)
        self.num1_entry.grid(column=1, row = 2)

        self.num2_entry = ttk.Entry(self, width=5)
        self.num2_entry.grid(column=3, row=2)

        self.calc_button = ttk.Button(self, text='Calculate',
                command=self.calculate)
        self.calc_button.grid(column=0, row=3, columnspan=4)
        #Label 
        self.answer_frame = ttk.LabelFrame(self, text='Grams Needed',
                height=100)
        self.answer_frame.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.answer_label = ttk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=0)
        #Label 2
        self.answer_frame2 = ttk.LabelFrame(self, text='Grams of a 10% Solution',
                height=100)
        self.answer_frame2.grid(column=0, row=5, columnspan=4, sticky='nesw')

        self.answer_label2 = ttk.Label(self.answer_frame2, text='')
        self.answer_label2.grid(column=0, row=0)
        #Label 3
        self.answer_frame3 = ttk.LabelFrame(self, text='Grams of a 1% Solution',
                height=100)
        self.answer_frame3.grid(column=0, row=6, columnspan=4, sticky='nesw')

        self.answer_label3 = ttk.Label(self.answer_frame3, text='')
        self.answer_label3.grid(column=0, row=0)
        

        # Labels that remain constant throughout execution.
        ttk.Label(self, text='Tasting Solution Calculator').grid(column=0, row=0,
                columnspan=4)
        ttk.Label(self, text='Desired PPM').grid(column=0, row=2,
                sticky='w')
        ttk.Label(self, text='mL').grid(column=2, row=2,
                sticky='w')

        ttk.Separator(self, orient='horizontal').grid(column=0,
                row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.root.bind('<Return>', lambda event: self.calculate())


if __name__ == '__main__':
    root = tk.Tk()
    Adder(root)
    root.mainloop()
