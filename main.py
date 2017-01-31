import engine.DriveControls as controls
import engine.config.Configuration as cfg
import engine.GPIO as GPIO
import time
import scripts.BrightSpot as spot

print('1 = BrightSpot')
choice = input('selecteer een script:')

def choose(choice):
    if(choice == 1):
        spot.start()
    else:
        choose(input('dit is geen optie'))
    