import engine.config.Configuration as Config
import engine.GPIO as gp
import util.logger as log
import time


def stop_motors():
    gp.pwmMotorAF.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorAB.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorBF.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorBB.ChangeDutyCycle(Config.defaultValues['stop'])
    log.logger.info("Stopped motors")
    #print(Config.defaultValues['dutyCycleA'])


def drive_forward():
    gp.pwmMotorAF.ChangeDutyCycle(Config.defaultValues['dutyCycleA'])
    gp.pwmMotorAB.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorBF.ChangeDutyCycle(Config.defaultValues['dutyCycleB'])
    gp.pwmMotorBB.ChangeDutyCycle(Config.defaultValues['stop'])
    log.logger.info("Started driving forward")
    #time.sleep(1)


def drive_backward():
    gp.pwmMotorAF.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorAB.ChangeDutyCycle(Config.defaultValues['dutyCycleA'])
    gp.pwmMotorBF.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorBB.ChangeDutyCycle(Config.defaultValues['dutyCycleB'])
    log.logger.info("Started driving backward")


def turn_left():
    gp.pwmMotorAF.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorAB.ChangeDutyCycle(Config.defaultValues['dutyCycleA'])
    gp.pwmMotorBF.ChangeDutyCycle(Config.defaultValues['dutyCycleB'])
    gp.pwmMotorBB.ChangeDutyCycle(Config.defaultValues['stop'])
    log.logger.info("Started turning left")


def turn_right():
    gp.pwmMotorAF.ChangeDutyCycle(Config.defaultValues['dutyCycleA'])
    gp.pwmMotorAB.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorBF.ChangeDutyCycle(Config.defaultValues['stop'])
    gp.pwmMotorBB.ChangeDutyCycle(Config.defaultValues['dutyCycleB'])
    log.logger.info("Started turning right")


def avoid_obstacle():
    # Turn right
    log.logger.info("Trying to avoid obstacle")
    turn_right()
    time.sleep(Config.defaultValues['turnTime'])
    stop_motors()


def stop_engine():
    log.logger.info("Stopping engine")
    stop_motors()
    gp.clear()
    log.logger.info("Stopped engine")
