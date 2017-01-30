import RPi.GPIO as GPIO
import engine.config.Configuration as cfg
import util.logger as log

def checkLineFollower():
    if(GPIO.input(cfg.pinmap['lineFollower']) == 0):
        log.logger.info('The line follow sensor is seeing a black surface')
        return True
    else:
        log.logger.info('The line follow sensor is seeing a white surface')
        return False