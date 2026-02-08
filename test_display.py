from inky.auto import auto 
from PIL import Image, ImageDraw 

display = auto() 

img = Image.new("P", display.resolution, 255)
draw = ImageDraw.Draw(img)
draw.text((10,10), "Hello, Inky!", fill=0) 

display.set_image(img) 
display.show() 


