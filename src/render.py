import os 
from PIL import Image, ImageOps

# TODO: define modular icon_path 

# for now... 


def get_tinted_icon(icon_path, color_tuple, size = None):
    """
    Gets an icon from the `assets` folder
    adds color to icon 
    :args: 
    icon_path: path to asset.png
    color_tuple: RGB tuple 
    size: tuple to resize icon 
    """
    icon = Image.open(icon_path).convert("RGBA")
    if size: 
        icon = icon.resize(size, Image.Resampling.LANCZOS)
    
    r, g, b, alpha = icon.split()

    gray_icon = icon.convert("L")

    tinted_icon = ImageOps.colorize(gray_icon, black=color_tuple, white="white")

    tinted_icon.putalpha(alpha)

    return tinted_icon 

def get_icon_from_weather():
    """
    
    """