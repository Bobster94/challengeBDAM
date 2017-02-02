import engine.modules.LineFollower as l
import engine.DriveControls as controls
import engine.modules.UltrasonicSensor as sensor
import util.logger as log
import engine.GPIO as GPIO
import time


def start():
    try:
        i = 1
        while True:
            if not l.is_over_black():
                controls.drive_forward()
                if sensor.is_near_obstacle(15):
                    controls.stop_motors()
                    if i == 1:
                        controls.turn_right()
                        time.sleep(1)
                        i = 0
                    else:
                        controls.turn_left()
                        time.sleep(1)
                        i = 1
            else:
                j = 1
                while True:
                    controls.turn_right()
                    if j == 1:
                        #turnOn()
                        j = 0
                        time.sleep(0.5)
                    else:
                        #turnOff()
                        j = 1
                        time.sleep(0.5)
                    time.sleep(5)
                controls.stop_motors()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.clear()