from evdev import InputDevice, categorize, ecodes
import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    if "Lic Pro" in device.name:
        controller = InputDevice(device.path)
        break

A_BUTTON = 305
B_BUTTON = 304
Y_BUTTON = 306
X_BUTTON = 307
D_UP = {'code':17, 'type': 3, 'value':-1}
D_RIGHT = {'code': 16, 'type': 3, 'value': 1}
D_DOWN = {'code':17, 'type':3, 'value':1}
D_LEFT = {'code':16, 'type':3, 'value':-1}
x_button = False
y_button = False
a_button = False
b_button = False
d_up = False
d_down = False
d_right = False
d_left = False
while True:
    for event in controller.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.code == x_button:
                if event.value == 1:
                    x_button = True
                elif event.value == 0:
                    x_button = False
            elif event.code == y_button:
                if event.value == 1:
                    y_button = True
                elif event.value == 0:
                    y_button = False
            elif event.code == b_button:
                if event.value == 1:
                    b_button = True
                elif event.value == 0:
                    b_button = False
            elif event.code == a_button:
                if event.value == 1:
                    a_button = True
                elif event.value == 0:
                    a_button = False
        if event.code == D_UP['code'] and event.type == D_UP['type']:
            if event.value == D_UP['value']:
                d_up = True
            else:
                d_up = False
        if event.code == D_DOWN['code'] and event.type == D_DOWN['type']:
            if event.value == D_DOWN['value']:
                d_down = True
            else:
                d_down = False
        if event.code == D_LEFT['code'] and event.type == D_LEFT['type']:
            if event.value == D_LEFT['value']:
                d_left = True
            else:
                d_left = False
        if event.code == D_RIGHT['code'] and event.type == D_RIGHT['type']:
            if event.value == D_RIGHT['value']:
                d_right = True
            else:
                d_right = False
