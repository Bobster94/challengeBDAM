import engine.modules.UltrasonicSensor as Sensor
import engine.DriveControls as Controls
import util.logger as log
import engine.config.Configuration as Config
import engine.GPIO as GPIO
import time
import random


def start():
    while True:
    	distance = Sensor.measure()
    	if time.sleep(random.randint2(1, 5)):
    		GoogleCar.newdirection()
        	GoogleCar.newdirection()
        else:Controls.drive_forward():
    	
    	

def newdirection():
		while (ultra.IsNearObstacle(cfg.defaultValues['minDistance'])):
            Controls.stopMotors()
            log.logger.info("choosing a new direction")
    		Controls.turnRight()
    		time.sleep(random.randint4(1, 5))
    		Controls.stopMotors()
		Controls.drive_forward()