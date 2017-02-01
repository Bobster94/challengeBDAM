import engine.modules.UltrasonicSensor as Sensor
import engine.DriveControls as Controls
import util.logger as log
import engine.GPIO as GPIO
import time

tick_delay = 0.6


def start():
    try:
        while True:
            #Controls.stop_motors()
            #time.sleep(0.1)
            #if not Sensor.is_near_obstacle(100):
            #    Controls.stop_motors()
            #    look_for_nearest_object()
            #elif Sensor.is_near_obstacle(10):
            #    Controls.stop_motors()
            #else:
            #    Controls.drive_forward()
            #    time.sleep(1)
            if Sensor.is_near_obstacle(50):
                Controls.drive_forward()
                time.sleep(1)
            elif Sensor.is_near_obstacle(20):
                Controls.stop_motors()
            else:
                Controls.stop_motors()
                time.sleep(0.3)
                look_for_nearest_object()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.clear()


def look_for_nearest_object():
    log.logger.info('searching for nearest object within 200cm')
    distance = Sensor.measure()
    while distance > 50:
        distance = Sensor.measure()

        log.logger.debug('current distance looking: ' + str(distance))
        Controls.stop_motors()
        time.sleep(0.5)
        Controls.turn_left()
        time.sleep(0.2)
        Controls.stop_motors()
        time.sleep(0.5)