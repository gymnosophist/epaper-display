# layout 
LAYOUT = {
    "current": {"x": 400, "y": 120, "icon_size": 200},
    "hourly" : {"y_start": 250, "x_start": 50, "spacing": 90}, 
    "daily" : {"y_start": 380, "x_start": 60, "spacing": 150}
},

# colors 
COLORS = {
    "clear": (255, 165, 0),    # Orange
    "cloudy": (128, 128, 128), # Gray
    "rain": (0, 0, 255),       # Blue
    "storm": (255, 0, 0),      # Red
    "text_main": (0, 0, 0)     # Black
},

ZONES = {
'Left':	{
    'x':220, 
    'y' : 60, 
    'anchor':'mm',
    'content':'dt'
    },
'Center': {
    'x':400,
      'y': 60, 
      'anchor':'mm',
      'content':
      'location'
      },	
'Right' : {
    'x':666, 
    'y': 60, 
    'anchor':'mm',
    'content':'current_temp'
    }, 
'Graph': {
    'left': 50, 
    'top': 150, 
    'right':750, 
    'bottom' : 320
    }
}

## do we need header / center / footer sections for the ZONES dict? 