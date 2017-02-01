import RPi.GPIO as GPIO
import engine.config.Configuration as Config
import util.logger as log
import engine.DriveControls as Controls
import time


def is_over_black():
    if GPIO.input(Config.pinmap['lineFollower']) == 0:
        # log.logger.info('The line follow sensor is seeing a black surface')
        return True
    else:
        # log.logger.info('The line follow sensor is seeing a white surface')
        return False


def seek_line():
    log.logger.debug('Seeking line')
    direction = True

    seek_size = 0.25
    seek_count = 1
    max_seek_count = 5

    while seek_count <= max_seek_count:
        time.sleep(0.2)
        seek_time = seek_size * seek_count
        if direction:
            log.logger.debug('Looking left')
            Controls.turn_left()
        else:
            log.logger.debug('looking right')
            Controls.turn_right()
        start_time = time.time()

        while time.time() - start_time <= seek_time:
            if is_over_black():
                Controls.stop_motors()
                return True
        Controls.stop_motors()

        seek_count += 1

        direction = not direction
    return False
