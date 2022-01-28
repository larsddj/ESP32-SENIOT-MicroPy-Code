import time
from machine import Pin, ADC
from measurements import MQMeasurement, MicrophoneMeasurement, HumidTempMeasurement

mqSensorPin = 39 # the GPIO pin the MQ-135 sensor is plugged into on the ESP32
micSensorPin = 34 # the GPIO pin the microphone sensor is plugged into on the ESP32

# these sensor methods retrieve measurements from a sensor and attach a timestamp object
# these measurements and timestamps are used for JSON serialization in createMeasurementJson.py

def get_microphone_measurements():
    clockStart = time.time_ns()
    micSensor = Pin(micSensorPin, Pin.IN)         

    micReading = MicrophoneMeasurement(micSensor.read())
    clockEnd = time.time_ns()
    timeSpentMs = (clockEnd-clockStart)/1000000
    
    micReading.setTimeSpent(timeSpentMs) 
    return micReading

def get_microphone_measurements_avg():
    clockStart = time.time_ns()
    micSensor = Pin(micSensorPin, Pin.IN)         
    
    # get an average of the given amount of samples
    i = 0
    micMeasurements = [] 
    while(i < mic_sample_amount):
        value = micSensor.value()
        micMeasurements.append(value)
        i+=1

    total = 0
    for x in micMeasurements:
        total+=x
    
    average = total/mic_sample_amount
    if(average < mic_cutoff_value):
        micAvgReading = MicrophoneMeasurement(1)
    else:
        micAvgReading = MicrophoneMeasurement(0)


    clockEnd = time.time_ns()
    timeSpentMs = (clockEnd-clockStart)/1000000
    micAvgReading.setTimeSpent(timeSpentMs)
    
    return micAvgReading

    
def get_mq_measurements():
    clockStart = time.time_ns()
    mqSensor = ADC(Pin(mqSensorPin))         
    mqSensor.atten(ADC.ATTN_11DB)   #This sets the maximum range of the sensor to 3.3v which is the input limit of the ESP32

    mqReading = MQMeasurement(mqSensor.read())

    clockEnd = time.time_ns()
    timeSpentMs = (clockEnd-clockStart)/1000000
    mqReading.setTimeSpent(timeSpentMs)

    return mqReading

def get_humTemp_measurements():
    clockStart = time.time()
    humTemp = HumidTempMeasurement(94, 33.45)
    clockEnd = time.time()
    timeSpentMs = clockEnd-clockStart
    
    humTemp.setTimeSpent(timeSpentMs)
    return humTemp