import datetime # for converting unix timestamps and displaying current local time 

from PIL import Image, ImageDraw, ImageFont
from inky.auto import auto  # Automatically detects the 7.3" display 
from src import weather, render 
import config 


icon_path = './assets/icon-pngs/wi-day-sunny.png'
#color_tuple = (255, 165, 0)
tinted_icon_small = render.get_tinted_icon(
    icon_path=icon_path,
    color_tuple=(255, 165, 0),
    size = (100,100)
)

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
    # note that we also have colors in config 
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)

    forecast = weather.get_weather() 

    current_temp = round(forecast['current']['temp'])
    
    # get dt for data 
    forecast_dt = datetime.datetime.fromtimestamp(forecast['current']['dt'])
    display_dt = forecast_dt.strftime('%b. %d %I:%M') 

    # load fonts 
    try:
        font_lg = ImageFont.truetype("assets/Inter/static/Inter_18pt-Bold.ttf", 80)
        font_sm = ImageFont.truetype("assets/Inter/static/Inter_24pt-Bold.ttf", 30)
    except IOError:
        print("Font not found, using default.")
        font_lg = font_sm = ImageFont.load_default()

    # 4. DESIGN CANVAS  

    # 4 a) Header area
    
    # draw datetime 
    draw.text(
        (config.ZONES['Left']['x'], config.ZONES['Left']['y']), 
        f'{display_dt}', 
        fill = BLACK,
        font = font_sm,
        anchor = 'rm'
        )
    # draw location 
    draw.text(
        (config.ZONES['Center']['x'], config.ZONES['Center']['y']), 
        "WASHINGTON, D.C.", 
        fill=BLACK, 
        font=font_sm,
        anchor = 'mm'
        )
    # draw current conditions 
    draw.text(
        (config.ZONES['Right']['x'], config.ZONES['Right']['y']), 
        f'{current_temp}', 
        fill = BLACK, 
        font = font_sm,
        anchor= 'lm'

    )
    # draw icon for current conditions 

    # anchor="mm" aligns the CENTER of the text to the coordinate.

    # Horizontal Divider (A thin Red line) -- designates end of header section 
    draw.line([30, 90, 770, 90], fill=RED, width=3)

    canvas.paste(tinted_icon_small, (550,0), tinted_icon_small)
    
    # 6. PUSH TO DISPLAY
    # This is the point of no return. 
    # It takes ~30 seconds on the 7.3" display.
    print("Updating display...")
    
    ###### 
    # commenting out for now 
    inky_display.set_image(canvas)
    inky_display.show()
    
    # 7. SAVE PREVIEW (For your SSH workflow)
    canvas.save("latest_render.png")
    print("Done! Preview saved to latest_render.png")

if __name__ == "__main__":
    main()

