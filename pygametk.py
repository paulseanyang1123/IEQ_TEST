import tkinter.messagebox
import pygame
import tkinter as tk
from tkinter import *
class PygameTk:
    def __init__(self):

        tk.Tk().withdraw()
        self.tk_root = tk.Tk()  # .withdraw()
        self.tk_root = Toplevel(bg="green")  # Tk()
        self.tk_root.geometry("30x25+30+900")
        self.tk_root.title('g')

        #self.tk_root.withdraw()

        #self.make_tk_widgets()
        select_palyers_input_area = Entry(self.tk_root, width=20).place(x=0, y=0)
        #self.bt = tk.Button(self.tk_root, text="Deal Card", font=25).place(x=50, y=30)  # , command=load_image
        #self.bt.pack()

        self.tk_root.mainloop()

        sys.stdout.flush()
    # def make_tk_widgets(self):
    #     #btn = tk.Button(self.tk_root, text='Start', command=self.toggle_to_pygame)
    #     bt = tk.Button(self.tk_root, text="Deal Card", font=25,command=load_image).place(x=1250, y=100)#,
    #     select_palyers = Label(root,text="Players Number (4/8)",font=25).place(x=160, y=10)
    #     select_palyers_input_area = Entry(root, width=20).place(x=240, y=10)
    #     #btn.pack()
    #     #bt.pack()
    #     self.tk_root.mainloop()