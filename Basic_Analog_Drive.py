#Created by Kepler Electronics, https://www.youtube.com/keplerelectronics

import explorerhat
import time
explorerhat.motor.one.invert()

from evdev import InputDevice, ecodes
while 1==1:
    try:
        fh = open('/dev/input/event0')
        print('controller found')
        gamepad = InputDevice('/dev/input/event0')
        print(gamepad)

        for event in gamepad.read_loop():
            if event.type == ecodes.EV_ABS:
                if event.code == 5:
                    if event.value > 155:
                        explorerhat.motor.one.forwards(event.value-155)
                    elif event.value < 100:
                        explorerhat.motor.one.backwards((100-event.value))
                    else:
                        explorerhat.motor.one.stop()
                elif event.code == 1:
                    if event.value > 155:
                        explorerhat.motor.two.forwards(event.value-155)
                    elif event.value < 100:
                        explorerhat.motor.two.backwards((100-event.value))
                    else:
                        explorerhat.motor.two.stop()
    except IOError:
        time.sleep(1)
        print('Controller Not Found')
