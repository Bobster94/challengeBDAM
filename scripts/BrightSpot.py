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
            if l.is_over_black():
                dist = sensor.measure()
                if dist <= 25 and dist > 2:
                    if count > 3:
                        Controls.drive_backward()
                        time.sleep(1)
                        if not l.is_over_black():
                            break
                        Controls.turn_right()
                        time.sleep(0.4)
                        if not l.is_over_black():
                            break
                    if not turn:
                        Config.defaultValues['defaultCycleA'] = 46  # de default value voor motor a
                        Config.defaultValues['defaultCycleB'] = 47  # de default value voor motor b
                        Controls.turn_right()
                        time.sleep(0.4)
                        if not l.is_over_black():
                            break
                        turn = True
                    else:
                        Config.defaultValues['defaultCycleA'] = 46  # de default value voor motor a
                        Config.defaultValues['defaultCycleB'] = 47  # de default value voor motor b
                        Controls.turn_left()
                        time.sleep(0.4)
                        if not l.is_over_black():
                            break
                        turn = False
                    count += 1
                else:
                    count = 0
                if sensor.measure() > 50:
                    Controls.drive_forward()
                    time.sleep(0.15)
                    if not l.is_over_black():
                        break
                    count = 0
                else:
                    Config.defaultValues['defaultCycleA'] = 46  # de default value voor motor a
                    Config.defaultValues['defaultCycleB'] = 47  # de default value voor motor b
                    Controls.drive_forward()
                    time.sleep(0.15)
                    if not l.is_over_black():
                        break
        Controls.stop_motors()
    except KeyboardInterrupt:
        GPIO.clear()