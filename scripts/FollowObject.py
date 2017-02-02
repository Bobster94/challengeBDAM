import engine.modules.UltrasonicSensor as Sensor
import engine.DriveControls as Controls
import util.logger as log
import engine.modules.LEDLamp as Lamp
import engine.config.Configuration as Config
import engine.GPIO as GPIO
import time

Config.defaultValues['frequency'] = 50 #de frequency voor dit script
defaultCycleA = 28 #de default value voor motor a
defaultCycleB = 25 #de default value voor motor b

max_distance = 176 #de maximale distance in centimeters


def start():#de functie naam
    try:# probeert
        turn_count = 0 #welke kant moet ik op count
        is_wall = 0 #is dit een muur count
        while True: #een loop om de code te herhalen
            Lamp.turn_on()
            distance = Sensor.measure() #distance wordt gemeten
            if distance < 15 and distance > 3: # als de distance kleiner dan 10 en groter dan 3 is voert hij het volgende
                Controls.stop_motors() # dit stopt motor
                is_wall += 1 #dit telt 1 op bij de muur counter
                if is_wall > 15: #als de muur counter groter dan 15 is voert hij dit uit
                    Lamp.turn_off()
                    is_wall = 0 #dit zet de muur counter naar 0
                    Controls.drive_backward() #rij vooruit
                    time.sleep(1) #slaap voor 1 seconde
                    Controls.turn_right() # draai naar rechts
                    time.sleep(1.5)#slaap voor anderhalve seconde
            elif distance > max_distance: #of als de distance groter is dan de maximale distance doe dit
                if turn_count <= 20 : #als de turn count kleiner of gelijk aan 20 is voer het volgende uit
                    Controls.turn_left() # draai naar links
                    turn_count += 1 #dit telt 1 bij de turn count op
                elif turn_count >= 20 and turn_count <= 40: #of als de turn count groter of gelijk aan 20 is en kleiner of gelijk aan 40 is doe het volgende
                    Controls.turn_right() # draai naar rechts
                    turn_count += 1 #dit telt 1 bij de turn count op
                else: #anders
                    turn_count = 0 #zet de turn count naar 0
            elif distance > 3: #of als de distance groter is dan 3
                if distance < 20: #als de distance kleiner is dan 20
                    Controls.drive_forward() #rijd naar voren
                else: #anders
                    Controls.drive_forward() #rijd naar voren
            time.sleep(0.15)#slaap voor 0.15 seconden
    except KeyboardInterrupt:#wanneer er op het toetsenbord word gedrukt stopt het script(ctrl+c)
        GPIO.clear()#stopt alles