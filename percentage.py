import psutil
from plyer import notification
import numpy as np



b = psutil.sensors_battery()
percentage = b.percent
print(b.percent)
print(b.power_plugged)

msg = ''

for i in range(5):
    fillArea = (percentage*18)//100
    # fillArea = 3
    for j in range(20):
        if i == 0:
            if j == 0:
                msg +=  "\u250C"
       
            elif j == 19:
                msg += "\u2510"
             
            else:
                msg += "\u2500"

        elif i == 4:
            if j == 0:
                msg +=  "\u2514"
       
            elif j == 19:
                msg += "\u2518"
             
            else:
                msg += "\u2500"
     
        else:
            if j == 19:
                if i == 1:
                   msg += "\u2514\u2510"
                elif i == 3:
                    msg += "\u250C\u2518"
                else:
                    msg += " \u2502"
            elif j == 0:
                msg += "\u2502"
            else:
   
                if fillArea != 0:
                    msg += "\u2591"
                    fillArea -= 1
                else:
                    msg += " "
                    

        
    msg += "\n"

print(msg)
# notification.notify(
#     title = 'test',
#     message = msg,
#     app_icon = "image1.ico",
#     timeout = 10,
# )
# print("\u2502  \u2591 \u2500 \u2514 \u2518 \u2510 \u250C")

# print("\u2500\u2510")

# print("\u2510\n\u2518")
# print(a)