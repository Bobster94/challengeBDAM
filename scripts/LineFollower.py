import engine.modules.LineFollower as LineFollower
import engine.DriveControls as Controls
import util.logger as log
import engine.GPIO as gp
import RPi.GPIO as GPIO
import engine.config.Configuration as Config
import time


def start():
    Config.defaultValues['frequency'] = 50
    Config.defaultValues['dutyCycleA'] = 35
    Config.defaultValues['dutyCycleB'] = 33
    random = 0
    try:
        while True:
            if LineFollower.is_over_black():
                Config.defaultValues['dutyCycleA'] = 25
                Config.defaultValues['dutyCycleB'] = 25
                Controls.stop_motors()
                Controls.drive_forward()
            else:
                Config.defaultValues['dutyCycleA'] = 25
                Config.defaultValues['dutyCycleB'] = 25
                Controls.stop_motors()
                Controls.drive_backward()

                if not LineFollower.seek_line():
                    Controls.drive_forward()
                    #log.logger.info('the robot has lost the line')
                    #exit()
                else:
                    log.logger.info('following the line')
            time.sleep(0.15)
            #Controls.stop_motors()
    except KeyboardInterrupt:
        Controls.stop_motors()
        GPIO.clear()
