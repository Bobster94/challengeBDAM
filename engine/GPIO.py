import RPi.GPIO as GPIO
import engine.config.Configuration as Config
import util.logger as log

log.logger.info("finalized initializing GPIO")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(Config.pinmap['motorAF'], GPIO.OUT)
GPIO.setup(Config.pinmap['motorAB'], GPIO.OUT)
GPIO.setup(Config.pinmap['motorBF'], GPIO.OUT)
GPIO.setup(Config.pinmap['motorBB'], GPIO.OUT)

GPIO.setup(Config.pinmap['lamp'], GPIO.OUT)

GPIO.setup(Config.pinmap['lineFollower'], GPIO.IN)

GPIO.setup(Config.pinmap['trigger'], GPIO.OUT)
GPIO.setup(Config.pinmap['echo'], GPIO.IN)

pwmMotorAF = GPIO.PWM(Config.pinmap['motorAF'], Config.defaultValues['frequency'])
pwmMotorAB = GPIO.PWM(Config.pinmap['motorAB'], Config.defaultValues['frequency'])
pwmMotorBF = GPIO.PWM(Config.pinmap['motorBF'], Config.defaultValues['frequency'])
pwmMotorBB = GPIO.PWM(Config.pinmap['motorBB'], Config.defaultValues['frequency'])

pwmMotorAF.start(Config.pinmap['motorAF'])
pwmMotorAB.start(Config.pinmap['motorAB'])
pwmMotorBF.start(Config.pinmap['motorBF'])
pwmMotorBB.start(Config.pinmap['motorBB'])


def clear():
    GPIO.cleanup()

# controls.driveForward()
