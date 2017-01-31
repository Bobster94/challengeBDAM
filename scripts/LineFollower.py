import engine.modules.LineFollower as l
import engine.DriveControls as controls
import util.logger as log
import engine.GPIO as GPIO
import time

def start():
    try:
        while True:
            if(l.isOverBlack()):
                controls.driveForward()
            else:
                controls.stopMotors()
                controls.driveBackward()
                time.sleep(1)
                if(l.seekLine() == False):
                    controls.stopMotors()
                    log.logger.info('the robot has lost the line')
                    exit()
                else:
                    log.logger.info('following the line')
    except KeyboardInterrupt:
        GPIO.clear()