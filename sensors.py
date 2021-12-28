import time
from machine import Pin, ADC
from measurements import MQMeasurement, MicrophoneMeasurement, HumidTempMeasurement

# these sensor methods retrieve measurements from a sensor and attach a timestamp object
# these measurements and timestamps are used for JSON serialization in createMeasurementJson.py

def get_microphone_measurements():
    clockStart = time.time()
    mic = MicrophoneMeasurement(100.34)
    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    
    mic.setTimeSpent(timeSpentMs) 
    return mic

def get_mq_measurements():
    clockStart = time.time()
    mqSensor = ADC(Pin(39))         #The GPIO pin the sensor is plugged into on the ESP32
    mqSensor.atten(ADC.ATTN_11DB)   #This sets the maximum range of the sensor to 3.3v which is the input limit of the ESP32

    mq = MQMeasurement(mqSensor.read())

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