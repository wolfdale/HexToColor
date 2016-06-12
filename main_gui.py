from Tkinter import *
import tkMessageBox
from PIL import ImageColor
from PIL import ImageTk
from PIL import Image
import Tkinter



class App(object):
    def __init__(self):
	self.root = Tk()
        self.root.geometry("200x200")
	self.root.wm_title("Hex To Color")
	
	self.label = Label (self.root, text= "Enter Hex Code")
        self.label.pack()
	self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Go")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.label = Label (self.root, text="")
        self.label.pack()

        self.root.mainloop()
