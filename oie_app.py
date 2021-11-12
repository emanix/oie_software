import tkinter.tix as tk
from tkinter.ttk import Label, Entry, Button, Frame, Treeview
import tkinter.messagebox as msgbox
from PIL import Image, ImageTk
from tkinter.tix import Balloon
import os
from tkinter import ttk, filedialog

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OIE Analytic Software")
        self.geometry('1161x653+103+40')
        #self.resizable(False, False)

        # Set icon image
        img = tk.PhotoImage(file='icons/data-analytics2.png')
        self.iconphoto(False, img)

        self.menu = tk.Menu(self, bg="lightgrey", fg="black")
        self.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open...', command=self.open_file, accelerator='Ctrl+O')
        file_menu.add_command(label='Exit', command=self.quit)


        image = Image.open("icons/folder.png")
        photo = ImageTk.PhotoImage(image)

        self.open_tip = Balloon(self)

        self.short_frame = tk.Frame(self, width=1161, height=65, bg="#99aadd")
        self.short_frame.pack(fill=tk.BOTH)
        self.short_frame.pack_propagate(0)

        self.open_shortcut_btn = tk.Button(self.short_frame, image=photo, bg="#99aadd", borderwidth=0)
        self.open_shortcut_btn.image = photo
        self.open_shortcut_btn.pack(side=tk.LEFT, padx=10, pady=5)

        self.open_tip.bind_widget(self.open_shortcut_btn, balloonmsg='Open...')

        self.table_frame = tk.Frame(self, width=1161, height=588)
        self.table_frame.pack(fill=tk.BOTH)
        self.table_frame.pack_propagate(0)

        table_display = ttk.Treeview()
        
        # self.open_shortcut_btn.bind("<Enter>", self.on_enter)
        # self.open_shortcut_btn.bind("<Leave>", self.on_leave)

        
    def open_file(self):
        filename = filedialog.askopenfilename(
            initialdir=os.path.join(os.path.expanduser('~'), "Documents")
        )

    # def on_enter(self, event):
    #     self.open_tip.configure(text="Open...")

    # def on_leave(self, enter):
    #     self.open_tip.configure(text="")

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()