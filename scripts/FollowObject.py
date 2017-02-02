import engine.modules.UltrasonicSensor as Sensor
import engine.DriveControls as Controls
import util.logger as log
import engine.config.Configuration as Config
import engine.GPIO as GPIO
import time

Config.defaultValues['frequency'] = 50
defaultCycleA = 25
defaultCycleB = 23


def start():
    try:
        time.sleep(5)
        max_distance = 100
        turn = True #false is right true is left
        while True:
            if Sensor.measure() < 70:
                Config.defaultValues['dutyCycleA'] = defaultCycleA
                Config.defaultValues['dutyCycleB'] = defaultCycleB
                time.sleep(0.05)
                Controls.drive_forward()
                time.sleep(0.05)
            else:
                if turn and Sensor.measure() > 70:
                    Config.defaultValues['dutyCycleA'] = defaultCycleA + 30
                    Config.defaultValues['dutyCycleB'] = defaultCycleA + 30
                    Controls.turn_left()
                    time.sleep(0.05)
                    if Sensor.measure() > 70:
                        Config.defaultValues['dutyCycleA'] = defaultCycleA
                        turn = True
                elif not turn and Sensor.measure() > 70:
                    Config.defaultValues['dutyCycleA'] = defaultCycleA + 20
                    Controls.turn_left()
                    time.sleep(0.05)
                    if Sensor.measure() > 40:
                        Config.defaultValues['dutyCycleA'] = defaultCycleA
                        turn = True
            #Controls.stop_motors()
            time.sleep(0.175)

    except KeyboardInterrupt:
        GPIO.clear()


def start2():
    while True:
        # Controls.stop_motors()
        # time.sleep(0.1)
        # if not Sensor.is_near_obstacle(100):
        #    Controls.stop_motors()
        #    look_for_nearest_object()
        # elif Sensor.is_near_obstacle(10):
        #    Controls.stop_motors()
        # else:
        #    Controls.drive_forward()
        #    time.sleep(1)
        count = 0
        turn_count = 0
        count2 = 0

        if Sensor.is_near_obstacle(100):
            Config.defaultValues['dutyCycleA'] = 35
            Config.defaultValues['dutyCycleB'] = 33
            distance = Sensor.measure()
            while distance > 20:
                Controls.drive_forward()
                time.sleep(0.1)
                distance = Sensor.measure()
        else:
            Config.defaultValues['dutyCycleA'] = 55
            Config.defaultValues['dutyCycleB'] = 58
            if turn_count < 6:
                Controls.turn_left()
                time.sleep(1.1)
                Controls.stop_motors()
                turn_count += 1
            else:
                Controls.drive_backward()
                time.sleep(1.5)
                turn_count = 0
        if Sensor.is_near_obstacle(10):
            if count < 3:
                Controls.stop_motors()
                Controls.drive_backward()
                count += 1
                # time.sleep(1)
            else:
                Config.defaultValues['dutyCycleA'] = 55
                Config.defaultValues['dutyCycleB'] = 58
                Controls.turn_left()
                # time.sleep(0.5)
                Controls.stop_motors()
                count = 0

        time.sleep(0.5)
        # time.sleep(0.5)
        # Controls.stop_motors()
        # time.sleep(0.2)