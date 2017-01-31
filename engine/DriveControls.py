import engine.config.Configuration as cfg
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
    time.sleep(1)

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

def turnRoundBigger():
    # recht om rondje maken steeds groter- Bobbie
    for x in xrange(0,50):
        x + 5
        gp.pwmMotorAF.ChangeDutyCycle(50)
        gp.pwmMotorAB.ChangeDutyCycle(cfg.defaultValues['stop'])
        gp.pwmMotorBF.ChangeDutyCycle(x)
        gp.pwmMotorBB.ChangeDutyCycle(cfg.defaultValues['stop'])
        if (l.isOverBlack()):
            x = 51
        else:
            log.logger.info("Gaat groter")
        time.sleep(1)

        log.logger.info("Making a circle")

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