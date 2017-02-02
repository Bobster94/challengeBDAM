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
        if time.sleep(random.randint(1, 5)):
            newdirection2()
        if distance < 10:
            newdirection()
        Controls.drive_forward()


def newdirection():
    while distance < 10:
        Controls.stop_motors()
        log.logger.info("choosing a new direction")
        Controls.turn_right()
        time.sleep(random.randint(1, 5))
        Controls.stop_motors()
        Controls.drive_forward()

def newdirection2():
        Controls.stop_motors()
        log.logger.info("choosing a new direction")
        Controls.turn_right()
        time.sleep(random.randint(1, 5))
        Controls.stop_motors()
        Controls.drive_forward()
        newdirection()