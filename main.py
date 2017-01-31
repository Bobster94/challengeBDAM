import engine.DriveControls as controls
import engine.config.Configuration as cfg
import RPi.GPIO as GPIO
import engine.modules.UltrasonicSensor as ultra
import time
try:
    GPIO.output(cfg.pinmap['trigger'], False)
    time.sleep(0.1)
    while True:
        controls.driveForward()
        time.sleep(0.1)
        if (ultra.IsNearObstacle(cfg.defaultValues['minDistance'])):
            controls.stopMotors()
            controls.avoidObstacle()
except KeyboardInterrupt:
    controls.stopEngine()