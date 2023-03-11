import psutil
from plyer import notification
import numpy as np

arr = np.array([[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0]])


b = psutil.sensors_battery()

print(b.percent)
print(b.power_plugged)

msg = ''

for i in range(6):
    for j in range(5):
        if(arr[i][j] == 1):
            msg += '\u2591'
        else:
            msg += ' '
    msg += '\n'
print(msg)
print('\033[0m')
notification.notify(
    title = 'test',
    message = msg,
    app_icon = "image1.ico",
    timeout = 10,
)
# print("\u2502  \u2591")