from Tkinter import *
import tkMessageBox
from PIL import ImageColor
from PIL import ImageTk
from PIL import Image
import Tkinter
from os import system


class App(object):
    def __init__(self):
	self.root = Tk()
        self.root.geometry("250x275")
	self.root.wm_title("Hex To Color")
	
	self.label = Label (self.root, text= "Enter Hex Code\n")
        self.label.pack()
        
	self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.label = Label (self.root, text="\n")
        self.label.pack()
	self.image_area = Canvas(self.root, width = 100, height = 100)
	self.image_area.pack()
        
        self.label = Label (self.root, text="\n")
        self.label.pack()
	self.buttontext = StringVar()
        self.buttontext.set("Go")
        Button(self.root, textvariable=self.buttontext, command=self.on_click).pack()

        self.label = Label (self.root, text="\n")
        self.label.pack()
	self.root.protocol("WM_DELETE_WINDOW",self.on_close_del_temp_file())
        self.root.mainloop()
    
    def on_click(self):
        hex_code = self.entrytext.get()
	hex_code = '#' + str(hex_code)
        self.hextocolor(str(hex_code))
	
	
	PILFile = Image.open('image.jpg')
	self.image_area.photo = ImageTk.PhotoImage(PILFile)
	
	self.image_area.delete('all')
	self.image_area.create_image(50,50,image=self.image_area.photo,anchor=CENTER)	
	
    def hextocolor(self, hex_code):
        rgb_tuple = ImageColor.getrgb(hex_code)
        image = Image.new('RGB',(120,120))
        color_list = []
        color_list.append(rgb_tuple)
        color_list = color_list * 14400
        image.putdata(color_list)
        image.save("image.jpg")


    def button_click(self, e):
        pass
    
    def on_close_del_temp_file(self):
	system("rm -f image.jpg")


if __name__=='__main__':
	App()
