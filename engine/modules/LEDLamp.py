import RPi.GPIO as GPIO
import engine.config.Configuration as Config


def turn_on():
    GPIO.output(Config.pinmap['lamp'], GPIO.HIGH)


def turn_off():
    GPIO.output(Config.pinmap['lamp'], GPIO.LOW)
