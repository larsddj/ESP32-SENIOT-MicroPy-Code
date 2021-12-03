import time

#Sensor lists are of variable size but always end with a timestamp
#for now the order of this is hardcoded (check docs) but this will most likely be OOP inheritance'd later on

def get_microphone_measurements():
    clockStart = time.time()
    #dict for values - hardcoded for now
    measurements = {
        "decibel":99,
        "timeSpentMs":None
    }
    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    
    print("these prints are from sensor.py")
    print(timeSpentMs)
    print(measurements)
    
    measurements["timeSpentMs"] = timeSpentMs 
    return measurements

def get_mq_measurements():
    clockStart = time.time()
    measurements = {
        "NH3":99,
        "NO2":99,
        "Alcohol":99,
        "Benzene":99,
        "Smoke":99,
        "CO2":99,
        "timeSpentMs":None
    }
    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    
    measurements["timeSpentMs"] = timeSpentMs 
    return measurements

def get_humTemp_measurements():
    clockStart = time.time()
    measurements = {
        "Humidity":99,
        "Temperature":99,
        "timeSpentMs":None
    }
    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    
    measurements["timeSpentMs"] = timeSpentMs 
    return measurements