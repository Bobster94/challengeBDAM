import RPi.GPIO as GPIO
import engine.config.Configuration as Config


def turn_on():
    GPIO.output(Config.pinmap['lamp1'], GPIO.HIGH)
    GPIO.output(Config.pinmap['lamp2'], GPIO.HIGH)

def turn_off():
    GPIO.output(Config.pinmap['lamp1'], GPIO.LOW)
    GPIO.output(Config.pinmap['lamp2'], GPIO.LOW)
