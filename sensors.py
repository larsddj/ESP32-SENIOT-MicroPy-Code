import time
from measurements import MQMeasurement, MicrophoneMeasurement, HumidTempMeasurement

#Sensor lists are of variable size but always end with a timestamp
#for now the order of this is hardcoded (check docs) but this will most likely be OOP inheritance'd later on

def get_microphone_measurements():
    clockStart = time.time()
    mic = MicrophoneMeasurement(100.34)
    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    
    mic.setTimeSpent(timeSpentMs) 
    return mic

def get_mq_measurements():
    clockStart = time.time()
    mq = MQMeasurement(100,99,88,33,203,1234)

    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    mq.setTimeSpent(timeSpentMs)

    return mq

def get_humTemp_measurements():
    clockStart = time.time()
    humTemp = HumidTempMeasurement(94, 33.45)
    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    
    humTemp.setTimeSpent(timeSpentMs)
    return humTemp