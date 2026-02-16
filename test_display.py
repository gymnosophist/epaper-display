from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont

# Initialize the display
display = auto()

# 1. Create a blank image with the Inky-specific palette
# 'P' mode is correct, but we'll let Inky handle the mapping later
img = Image.new("P", display.resolution)
draw = ImageDraw.Draw(img)

# 2. Try to load a readable font (standard on most Pis)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
except IOError:
    font = ImageFont.load_default()

# 3. Draw some color! 
# (Inky Impression colors: 0=Black, 1=White, 2=Green, 3=Blue, 4=Red, 5=Yellow, 6=Orange)
draw.text((60, 180), "Hello Inky Impression", fill=4, font=font) # Red text

# 4. Display the image
display.set_image(img)
display.show()