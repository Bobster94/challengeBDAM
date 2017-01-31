import RPi.GPIO as GPIO
import engine.config.Configuration as cfg
import util.logger as log
import engine.DriveControls as controls
import time

def isOverBlack():
    if(GPIO.input(cfg.pinmap['lineFollower']) == 0):
        #log.logger.info('The line follow sensor is seeing a black surface')
        return True
    else:
        #log.logger.info('The line follow sensor is seeing a white surface')
        return False
def seekLine():
    log.logger.debug('Seeking line')
    direction = True
    
    seekSize = 0.25
    seekCount = 1
    maxSeekCount = 5
    
    while(seekCount <= maxSeekCount):
        
        seekTime = seekSize * seekCount
        if(direction):
            log.logger.debug('Looking left')
            controls.turnLeft()
        else:
            log.logger.debug('looking right')
            controls.turnRight()
        startTime = time.time()
        
        while(time.time()-startTime <= seekTime):
            if(isOverBlack()):
                controls.stopMotors()
                return True
        controls.stopMotors()
        
        seekCount += 1
        
        direction = not direction
    return False