import RPi.GPIO as GPIO
import engine.config.Configuration as cfg

def turnOn():
    GPIO.output(cfg.pinmap['lamp'], GPIO.HIGH)
def turnOff():
    GPIO.output(cfg.pinmap['lamp'], GPIO.LOW)
