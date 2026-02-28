import datetime # for converting unix timestamps and displaying current local time 


from PIL import Image, ImageDraw, ImageFont
from inky.auto import auto  # Automatically detects the 7.3" display 
from src import weather

def main(): 
    """
    Tests the display and pushes an image based on the weather 
    """
    # Initialize display 

    inky_display = auto() 

    # Create canvas 

    width, height = 800, 480 

    canvas = Image.new(
        mode="RGB", 
        size=(width, height), 
        color = (255, 255, 255) # white background 
        )
    
    draw = ImageDraw.Draw(canvas)

    # 3. DEFINE COLORS (Spectra 6 Friendly)
    # Using pure RGB values ensures the driver maps them correctly.
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)

    current_weather = weather.get_weather() 
    # get current_temperature 
    current_temp = current_weather()['current']['temp']

    # load fonts 
    try:
        font_lg = ImageFont.truetype("assets/Inter/static/Inter_18pt-Bold.ttf", 80)
        font_sm = ImageFont.truetype("assets/Inter/static/Inter_24pt-Bold.ttf", 30)
    except IOError:
        print("Font not found, using default.")
        font_lg = font_sm = ImageFont.load_default()
    # 4. Draw a box 
    draw.rectangle([0, 0, 280, 480], fill=BLACK)

    # Temperature Text (Centered in the sidebar)
    # anchor="mm" aligns the CENTER of the text to the coordinate.
    draw.text((140, 240), f"{current_temp}°", fill=WHITE, font=font_lg, anchor="mm")
    
    # Header area
    draw.text((310, 40), "WASHINGTON, D.C.", fill=BLACK, font=font_sm)
    
    # Horizontal Divider (A thin Red line)
    draw.line([310, 85, 770, 85], fill=RED, width=3)

    # 6. PUSH TO DISPLAY
    # This is the point of no return. 
    # It takes ~30 seconds on the 7.3" display.
    print("Updating display...")
    inky_display.set_image(canvas)
    inky_display.show()
    
    # 7. SAVE PREVIEW (For your SSH workflow)
    canvas.save("latest_render.png")
    print("Done! Preview saved to latest_render.png")

if __name__ == "__main__":
    main()

