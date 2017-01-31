import engine.config.Configuration as cfg
import RPi.GPIO as GPI
import engine.GPIO as gp
import util.logger as log
import time

def stopMotors():
    gp.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['stop'])
    log.logger.info("Stopped motors")

def driveForward():
    gp.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    gp.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
    gp.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['stop'])
    log.logger.info("Started driving forward")

def driveBackward():
    gp.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    gp.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
    log.logger.info("Started driving backward")

def turnLeft():
    gp.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    gp.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
    gp.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['stop'])
    log.logger.info("Started turning left")

def turnRight():
    gp.pwmMotorAF.ChangeDutyCycle(cfg.defaultValues['dutyCycleA'])
    gp.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorBF.ChangeDutyCycle(cfg.defaultValues['stop'])
    gp.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['dutyCycleB'])
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
    gp.clear()
    log.logger.info("Stopped engine")