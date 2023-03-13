import psutil
from plyer import notification
import numpy as np
HEIGHT = 5 #shoud be odd
WIDTH = 20


b = psutil.sensors_battery()
percentage = b.percent
isPlugged = b.power_plugged
print(b.percent)
print(b.power_plugged)
print((percentage*18)//100)
battery = ''

for i in range(HEIGHT):
    fillArea = (percentage*(WIDTH-2))//100
    # fillArea = 3
    for j in range(WIDTH):
        if i == 0:
            if j == 0:
                battery +=  "\u250C"
       
            elif j == WIDTH-1:
                battery += "\u2510"
             
            else:
                battery += "\u2500"

        elif i == HEIGHT-1:
            if j == 0:
                battery +=  "\u2514"
       
            elif j == WIDTH-1:
                battery += "\u2518"
             
            else:
                battery += "\u2500"
     
        else:
            if j == WIDTH-1:
                if i == (HEIGHT//2)-1:
                   battery += "\u2514\u2510"
                elif i == (HEIGHT//2)+1:
                    battery += "\u250C\u2518"
                elif i == (HEIGHT//2):
                    if isPlugged:
                        battery += " \u2502\u26A1"
                    else:
                        battery += " \u2502"
                else:
                    battery += "\u2502"
            elif j == 0:
                battery += "\u2502"
            else:
                
                if fillArea != 0:
                    if isPlugged:
                        battery += "\033[42m "
                    else:
                        battery += "\033[47m "
                    fillArea -= 1
                else:
                    battery += "\033[0m "
                    

        
    battery += "\n"

print(battery)
print("\033[0m")

print((7//2)-1)
# notification.notify(
#     title = 'test',
#     message = battery,
#     app_icon = "image1.ico",
#     timeout = 10,
# )
# print("\u2502  \u2591 \u2500 \u2514 \u2518 \u2510 \u250C")

# print("\u2500\u2510")

# print("\u2510\n\u2518")
# print("\u26A1")