import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7
pinTrigger = 17
pinEcho = 18
pinLamp = 21
# How many times to turn the pin on and off each second
Frequency = 50
# How long the pin stays on each cycle, as a percent (here, it's 30%)
DutyCycleA = 30 #float(input("set dutycycle for a: "))
DutyCycleB = 30 #float(input("set dutycycle for b: "))
#time1 = float(input("set time to ride"))
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0
# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinTrigger, GPIO.OUT) # Trigger
GPIO.setup(pinEcho, GPIO.IN) # Echo
GPIO.setup(pinLamp, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)
# Turn all motors off

def StopMotors():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors forwards
def Forwards():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors backwards
def Backwards():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
# Turn left
def Left():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn Right
def Right():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

time.sleep(10)	
try:
	while True:
		GPIO.output(pinTrigger, False)
		time.sleep(0.5)
		GPIO.output(pinTrigger, True)
		time.sleep(0.00001)
		GPIO.output(pinTrigger, False)
		StartTime = time.time()
		
		while GPIO.input(pinEcho)==0:
			StartTime = time.time()
		
		while GPIO.input(pinEcho)==1:
			StopTime = time.time()
			if StopTime-StartTime >= 0.04:
				print("Hold on there! You're too close for me to see.")
				StopTime = StartTime
				break
		ElapsedTime = StopTime - StartTime
		Distance = ElapsedTime * 34326
		Distance = Distance / 2
		
		if(Distance > 10):
			Forwards()
		else:
			StopMotors()
			GPIO.output(pinLamp, GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(pinLamp, GPIO.LOW)
		time.sleep(0.5)
except KeyboardInterrupt:
	StopMotors()
	GPIO.cleanup()