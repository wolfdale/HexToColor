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
