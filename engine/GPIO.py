import RPi.GPIO as GPIO
import engine.config.Configuration as cfg
import util.logger as log


log.logger.info("finalized initializing GPIO")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(cfg.pinmap['motorAF'], GPIO.OUT)
GPIO.setup(cfg.pinmap['motorAB'], GPIO.OUT)
GPIO.setup(cfg.pinmap['motorBF'], GPIO.OUT)
GPIO.setup(cfg.pinmap['motorBB'], GPIO.OUT)

GPIO.setup(cfg.pinmap['lamp'], GPIO.OUT)

GPIO.setup(cfg.pinmap['lineFollower'], GPIO.IN)

GPIO.setup(cfg.pinmap['trigger'], GPIO.OUT)
GPIO.setup(cfg.pinmap['echo'], GPIO.IN)

pwmMotorAF = GPIO.PWM(cfg.pinmap['motorAF'], cfg.defaultValues['frequency'])
pwmMotorAB = GPIO.PWM(cfg.pinmap['motorAB'], cfg.defaultValues['frequency'])
pwmMotorBF = GPIO.PWM(cfg.pinmap['motorBF'], cfg.defaultValues['frequency'])
pwmMotorBB = GPIO.PWM(cfg.pinmap['motorBB'], cfg.defaultValues['frequency'])

pwmMotorAF.start(cfg.pinmap['motorAF'])
pwmMotorAB.start(cfg.pinmap['motorAB'])
pwmMotorBF.start(cfg.pinmap['motorBF'])
pwmMotorBB.start(cfg.pinmap['motorBB'])

def clear():
    GPIO.cleanup()
    
#controls.driveForward()
