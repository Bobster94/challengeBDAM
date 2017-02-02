pinmap = {
    # pins waar de motors op staan
    'motorAF': 10,
    'motorAB': 9,
    'motorBF': 8,
    'motorBB': 7,

    # pin voor de lijn volger
    'lineFollower': 25,
    'test' : 2,
    # pin voor de led lampjes
    'lamp2' : 20,
    'lamp1': 21,

    # pins voor ultrasonic sensor
    'trigger': 17,
    'echo': 18
}

defaultValues = {
    # hoe vaak de pins aan en uit gaan per seconde
    'frequency': 100,

    # hoe lang de pin aan staat op elke cycle als een procent
    'dutyCycleA': 46,#43 #28
    'dutyCycleB': 47,#52 #26

    # stopt de cycle
    'stop': 0,

    'turnTime': 0.45,
    'reverseTime': 0.5,
    'minDistance': 15
}