import RPi.GPIO as GPIO
import engine.config.Configuration as cfg
import util.logger as log


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

#The frequency of power sent by the battery to the specified wheels, frequency is defined in: config>Configuration
pwmMotorAF = GPIO.PWM(cfg.pinmap['motorAF'], cfg.defaultValues['frequency'])
pwmMotorAB = GPIO.PWM(cfg.pinmap['motorAB'], cfg.defaultValues['frequency'])
pwmMotorBF = GPIO.PWM(cfg.pinmap['motorBF'], cfg.defaultValues['freqcorrectionAF'])
pwmMotorBB = GPIO.PWM(cfg.pinmap['motorBB'], cfg.defaultValues['frequency'])

log.logger.info("finalized initializing GPIO")

def clear():
    GPIO.cleanup()
