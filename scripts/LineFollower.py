import engine.modules.LineFollower as LineFollower
import engine.DriveControls as Controls
import util.logger as log
import engine.GPIO as GPIO
import engine.config.Configuration as Config
import time


def start():
    Config.defaultValues['frequency'] = 100
    try:
        while True:
            if LineFollower.is_over_black():
                Controls.drive_forward()
            else:
                Controls.stop_motors()
                Controls.drive_backward()
                #time.sleep(1)
                if not LineFollower.seek_line():
                    Controls.stop_motors()
                    log.logger.info('the robot has lost the line')
                    exit()
                else:
                    log.logger.info('following the line')
            time.sleep(0.05)
    except KeyboardInterrupt:
        Controls.stop_motors()
        GPIO.clear()
