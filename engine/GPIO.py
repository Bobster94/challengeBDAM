import RPi.GPIO as GPIO
import engine.config.Configuration as Config
import util.logger as log

log.logger.info("finalized initializing GPIO")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#zet alle GPIO pins voor de motor op output
GPIO.setup(Config.pinmap['motorAF'], GPIO.OUT)
GPIO.setup(Config.pinmap['motorAB'], GPIO.OUT)
GPIO.setup(Config.pinmap['motorBF'], GPIO.OUT)
GPIO.setup(Config.pinmap['motorBB'], GPIO.OUT)

#zet de GPIO pin voor lamp naar output
GPIO.setup(Config.pinmap['lamp2'], GPIO.OUT)
GPIO.setup(Config.pinmap['lamp1'], GPIO.OUT)

#zet de GPIO pin voor linefollower op input
GPIO.setup(Config.pinmap['lineFollower'], GPIO.IN)
#zet de trigger van de sensor op output
GPIO.setup(Config.pinmap['trigger'], GPIO.OUT)
#zet de echo van de sensor op input
GPIO.setup(Config.pinmap['echo'], GPIO.IN)

pwmMotorAF = GPIO.PWM(Config.pinmap['motorAF'], Config.defaultValues['frequency'])
pwmMotorAB = GPIO.PWM(Config.pinmap['motorAB'], Config.defaultValues['frequency'])
pwmMotorBF = GPIO.PWM(Config.pinmap['motorBF'], Config.defaultValues['frequency'])
pwmMotorBB = GPIO.PWM(Config.pinmap['motorBB'], Config.defaultValues['frequency'])

#start de motoren
pwmMotorAF.start(0)
pwmMotorAB.start(0)
pwmMotorBF.start(0)
pwmMotorBB.start(0)

def clear():
    GPIO.cleanup()

# controls.driveForward()
