import psutil

# specify height and width of the battery
HEIGHT = 5 #shoud be odd
WIDTH = 20

# take battery parameters
b = psutil.sensors_battery()
percentage = b.percent
isPlugged = b.power_plugged
percentage = 50
# initialze battery
battery = "\n"



for i in range(HEIGHT):

    # define color filling area according to the battery percentage
    fillArea = (percentage*(WIDTH-2))//100
    
    for j in range(WIDTH):
        battery += "\033[0m" #starting with resetting colors
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
                        battery += " \u2502\u26A1" # show plugging icon
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
                    elif percentage <= 10:
                        # if battery is low the color turned to red
                        battery += "\033[41m "
                    else:
                        battery += "\033[47m "

                    fillArea -= 1
                else:
                    battery += "\033[0m "
                    

        
    battery += "\n"

print(battery)
print("\033[0m")
