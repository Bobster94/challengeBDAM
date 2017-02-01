import RPi.GPIO as GPIO
import engine.config.Configuration as Config
import util.logger as log
import time


def measure():
    GPIO.output(Config.pinmap['trigger'], True)
    time.sleep(0.00001)
    GPIO.output(Config.pinmap['trigger'], False)
    start_time = time.time()
    stop_time = start_time
    while GPIO.input(Config.pinmap['echo']) == 0:
        start_time = time.time()
        stop_time = start_time
    while GPIO.input(Config.pinmap['echo']) == 1:
        stop_time = time.time()
        # If the sensor is too close to an object, the Pi cannot
        # see the echo quickly enough, so it has to detect that
        # problem and say what has happened
        if stop_time - start_time >= 0.04:
            log.logger.warning("Hold on there! You're too close for me to see.")
            stop_time = start_time
            break
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34326) / 2
    return distance


def is_near_obstacle(local_how_near):
    distance = measure()
    print("is near obstacle: " + str(distance))
    if distance < local_how_near:
        return True
    else:
        return False
