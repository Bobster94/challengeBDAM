import engine.modules.LineFollower as l
import engine.DriveControls as controls
import util.logger as log
import engine.GPIO as GPIO
import time

def start():
    try:
        i = 1
        while True:
            if(l.isOverWhite()):
                controls.driveForward()
                if IsNearObstacle(10):
                    stopMotors()
                    if (i = 1):
                        turnRight()
                        time.sleep(1)
                        i = 0
                    else:
                        turnLeft()
                        time.sleep(1)
                        i = 1
            else:
                controls.stopEngine()
                
    except KeyboardInterrupt:
        GPIO.clear()