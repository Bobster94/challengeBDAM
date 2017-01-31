pinmap = {
    #pins waar de motors op staan
    'motorAF' : 10,
    'motorAB' : 9,
    'motorBF' : 8,
    'motorBB' : 7,
    
    #pin voor de lijn volger
    'lineFollower' : 25,
    
    #pin voor de led lampjes
    'lamp' : 21,
    
    #pins voor ultrasonic sensor 
    'trigger' : 17,
    'echo' : 18
}

defaultValues = {
    #hoe vaak de pins aan en uit gaan per seconde
    'frequency' : 50,
    
    #hoe lang de pin aan staat op elke cycle als een procent
    'dutyCycleA' : 27.5,
    'dutyCycleB' : 28.7,
    
    #stopt de cycle
    'stop' : 0,
    
    'turnTime' : 0.45,
    'reverseTime' : 0.5,
    'minDistance' : 15
}