from PIL import ImageColor
from PIL import Image
import Tkinter

def hextocolor(hex_code):
	rgb_tuple = ImageColor.getrgb(hex_code)
	image = Image.new('RGB',(120,120))
	color_list = []
	color_list.append(rgb_tuple)
	color_list = color_list * 14400
	image.putdata(color_list)
	image.save("hola.jpg")


def GUI():
	main_window = Tkinter.Tk()
	main_window.mainloop()
if __name__=='__main__':
	GUI()
	hex_code = raw_input()
	hex_code = '#' + str(hex_code)
	print hex_code
	hextocolor(hex_code)
