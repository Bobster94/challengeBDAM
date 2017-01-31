import engine.DriveControls as controls
import engine.config.Configuration as cfg
import engine.GPIO as GPIO
import time
import scripts.LineFollower as line

print('1 = linefollower')
choice = input('selecteer een script:')

def choose(choice):
    if(choice == 1):
        line.start()
    else:
        choose(input('dit is geen optie'))
    