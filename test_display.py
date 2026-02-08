from inky.impression import InkyImpression
from PIL import Image, ImageDraw

display = InkyImpression()

img = Image.new("P", display.resolution, 255)
draw = ImageDraw.Draw(img)
draw.text((50, 50), "Hello Inky Impression", fill=0)

display.set_image(img)
display.show()