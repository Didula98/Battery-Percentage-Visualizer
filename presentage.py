import psutil
from plyer import notification
# import numpy as np

b = psutil.sensors_battery()

print(b.percent)
print(b.power_plugged)


notification.notify(
    title = 'Battery',
    message = str(b.percent) + ' ' + str(b.power_plugged),
    app_icon = "image1.ico",
    timeout = 10,
)
