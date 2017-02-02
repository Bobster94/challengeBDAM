import engine.modules.LineFollower as l
import engine.DriveControls as Controls
import engine.modules.UltrasonicSensor as sensor
import util.logger as log
import engine.config.Configuration as Config
import engine.GPIO as GPIO
import time

Config.defaultValues['frequency'] = 50 #de frequency voor dit script

def start():
    try:#test
        turn = False #false = rechts, true = links
        count = 0
        while True:
            if sensor.measure() <= 20:
                if count > 5:
                    Controls.drive_backward()
                    Controls.turn_right()
                    time.sleep(0.6)
                if not turn:
                    Config.defaultValues['defaultCycleA'] = 26  # de default value voor motor a
                    Config.defaultValues['defaultCycleB'] = 28  # de default value voor motor b
                    Controls.turn_right()
                    #time.sleep(0.6)
                    turn = True
                else:
                    Config.defaultValues['defaultCycleA'] = 26  # de default value voor motor a
                    Config.defaultValues['defaultCycleB'] = 28  # de default value voor motor b
                    Controls.turn_left()
                    #time.sleep(0.6)
                    turn = False
                count += 1
            else:
                count = 0
            if sensor.measure() > 50:
                Controls.drive_forward()
                time.sleep(0.15)
            else:
                Config.defaultValues['defaultCycleA'] = 26  # de default value voor motor a
                Config.defaultValues['defaultCycleB'] = 28  # de default value voor motor b
                Controls.drive_forward()
                time.sleep(0.15)
    except KeyboardInterrupt:
        GPIO.clear()