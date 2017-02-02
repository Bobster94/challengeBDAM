import engine.modules.UltrasonicSensor as Sensor
import engine.DriveControls as Controls
import util.logger as log
import engine.config.Configuration as Config
import engine.GPIO as GPIO
import time

def start():
    	if time.sleep(cfg.defaultValues[random.randint2(1, 5)])
            controls.stopMotors()
            log.logger.info("Trying to avoid obstacle")
    		turnRight()
    		time.sleep(random.randint3(1, 5))
    		stopMotors()
		.drive_forward()
    	
    	while (ultra.IsNearObstacle(cfg.defaultValues['minDistance'])):
            controls.stopMotors()
            log.logger.info("choosing a new direction")
    		turnRight()
			random.randint(1, 5)
    		time.sleep(random.randint4(1, 5))
    		stopMotors()
		controls.drive_forward()
