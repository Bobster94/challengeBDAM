import engine.modules.LineFollower as l
import engine.DriveControls as controls
import util.logger as log
import engine.GPIO as GPIO
import time

def start():
    try:
        while True:
            if(l.isOverBlack()):
                controls.driveForward()
            else:
                controls.stopMotors()
                controls.driveBackward()
                time.sleep(0.5)
                if(l.seekLine() == False):
                    controls.stopMotors()
                    log.logger.info('the robot has lost the line')
                    # Bob ingevoegd regel 19 - 20
                    controls.turnRoundBigger()
                    exit()
                else:
                    log.logger.info('following the line')
    except KeyboardInterrupt:
        GPIO.clear()

#  Bobbie opzetje alles uitgecomment kijk maar even wat wel en niet gebruiken en hoe dit intepeteren
#  Autotje verliest lijn kijkt 0.1 sec rechts geen lijn? kijkt 0.1 * 2 Links zwartelijn ga rechtuit.

# def start():
#     try:
#         while True:
#             if(l.isOverBlack()):
#                 controls.driveForward()
#                 i = 1
#             else:
#                 controls.stopMotors()
#                 # doe max 3 x anders gaat tever van de lijn weg
#                 if i < 4:
#                     # kijk 1x rechts & 2x links (lijn gevonden ga weer rechtuit)
#                     controls.turnRight()
#                     time.sleep(0.1)
#                     controls.turnLeft()
#                     time.sleep(0.2)
#                     i + 1
#                 else:
#                     if(l.seekLine() == False):
#                         controls.stopMotors()
#                         log.logger.info('the robot has lost the line')
#                         controls.turnRoundBigger()
#                         exit()
#                     else:
#                         log.logger.info('following the line')
#     except KeyboardInterrupt:
#         GPIO.clear()