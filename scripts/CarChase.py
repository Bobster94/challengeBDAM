import engine.GPIO as GPIO
import engine.DriveControls as Controls
import engine.modules.UltrasonicSensor as Sensor
import engine.config.Configuration as Config
import time

Config.defaultValues['frequency'] = 1
defaultCycleA = 28
defaultCycleB = 26


def start():
    try:
        time.sleep(5)
        turn = True #false is right true is left
        while True:
            if Sensor.measure() < 30 and Sensor.measure() > 3:
                Config.defaultValues['dutyCycleA'] = defaultCycleA
                Config.defaultValues['dutyCycleB'] = defaultCycleB
                Controls.drive_forward()
            else:
                if turn and Sensor.measure() > 30:
                    #Config.defaultValues['dutyCycleA'] = defaultCycleA + 20
                    Controls.turn_left()
                    time.sleep(0.2)
                    if Sensor.measure() > 30:
                        Config.defaultValues['dutyCycleA'] = defaultCycleA
                        turn = False
                elif not turn and Sensor.measure() > 30:
                    #Config.defaultValues['dutyCycleB'] = defaultCycleB + 20
                    Controls.turn_right()
                    time.sleep(0.2)
                    if Sensor.measure() > 30:
                        Config.defaultValues['dutyCycleB'] = defaultCycleB
                        turn = True
            #Controls.stop_motors()
            time.sleep(0.05)

    except KeyboardInterrupt:
        GPIO.clear()