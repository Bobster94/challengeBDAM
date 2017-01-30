import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinLineFollower = 25
count = 0
GPIO.setup(pinLineFollower, GPIO.IN)
try:
	while True:
		if GPIO.input(pinLineFollower)==0:
			print('The sensor is seeing a black surface')
		else:
			print('The sensor is seeing a white surface')
		count += 1
		print(count)
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
