import engine.config.Configuration as cfg
import engine.GPIO as GPIO
import util.logger as log
import time

def stopMotors():
    GPIO.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['stop'])
    log.logger.info("Stopped motors")

def driveForward():
    GPIO.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    GPIO.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
    GPIO.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['stop'])
    log.logger.info("Started driving forward")

def driveBackward():
    GPIO.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    GPIO.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
    log.logger.info("Started driving backward")

def turnLeft():
    GPIO.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    GPIO.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
    GPIO.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['stop'])
    log.logger.info("Started turning left")

def turnRight():
    GPIO.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    GPIO.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['stop'])
    GPIO.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
    log.logger.info("Started turning right")

def avoidObstacle():
# Turn right
    log.logger.info("Trying to avoid obstacle")
    turnRight()
    time.sleep(cfg.defaultValues['turnTime'])
    stopMotors()

def stopEngine():
    log.logger.info("Stopping engine")
    stopMotors()
    GPIO.clear()
    log.logger.info("Stopped engine")