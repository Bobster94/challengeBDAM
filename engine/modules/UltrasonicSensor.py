import RPi.GPIO as GPIO
import engine.config.Configuration as cfg
import util.logger as log
import time

def Measure():
    GPIO.output(cfg.pinmap['trigger'], True)
    time.sleep(0.00001)
    GPIO.output(cfg.pinmap['trigger'], False)
    StartTime = time.time()
    StopTime = StartTime
    while GPIO.input(cfg.pinmap['echo'])==0:
        StartTime = time.time()
        StopTime = StartTime
    while GPIO.input(cfg.pinmap['echo'])==1:
        StopTime = time.time()
# If the sensor is too close to an object, the Pi cannot
# see the echo quickly enough, so it has to detect that
# problem and say what has happened
        if (StopTime-StartTime >= 0.04):
            log.logger.warning("Hold on there! You're too close for me to see.")
            StopTime = StartTime
            break
    ElapsedTime = StopTime - StartTime
    Distance = (ElapsedTime * 34326)/2
    return Distance

def IsNearObstacle(localHowNear):
    Distance = Measure()
    print("IsNearObstacle: "+str(Distance))
    if Distance < localHowNear:
        return True
    else:
        return False