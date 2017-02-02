import engine.modules.UltrasonicSensor as Sensor
import engine.DriveControls as Controls
import util.logger as log
import engine.config.Configuration as Config
import engine.GPIO as GPIO
import time
import random


def start():
    while True:
        distance = Sensor.measure()
        time.sleep(random.randint(1, 5))
        newdirection()
        newdirection()
        Controls.drive_forward()


def newdirection():
    while (Sensor.measure() <= 10):
        Controls.stop_motors()
        log.logger.info("choosing a new direction")
        Controls.turn_right()
        time.sleep(random.randint(1, 5))
        Controls.stop_motors()
        Controls.drive_forward()