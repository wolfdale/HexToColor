from Tkinter import *
import tkMessageBox
from PIL import ImageColor
from PIL import ImageTk
from PIL import Image
import Tkinter



class App(object):
    def __init__(self):
	self.root = Tk()
        self.root.geometry("250x250")
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
    def clicked1(self):
        hex_code = self.entrytext.get()
	hex_code = '#' + str(hex_code)
        self.hextocolor(str(hex_code))
	
	self.image_area = Canvas(self.root, width = 120, height = 120)
	self.image_area.pack()
	
	PILFile = Image.open('image.jpg')
	self.image_area.photo = ImageTk.PhotoImage(PILFile)
	
	self.image_area.delete('all')
	self.image_area.create_image(100,100,image=self.image_area.photo,anchor=CENTER)	

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



if __name__=='__main__':
	App()
