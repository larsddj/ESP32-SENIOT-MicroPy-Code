import time
from machine import Pin, ADC
from measurements import MQMeasurement, MicrophoneMeasurement, HumidTempMeasurement

mqSensorPin = 39 # the GPIO pin the MQ-135 sensor is plugged into on the ESP32
micSensorPin = 34 # the GPIO pin the microphone sensor is plugged into on the ESP32

# these sensor methods retrieve measurements from a sensor and attach a timestamp object
# these measurements and timestamps are used for JSON serialization in createMeasurementJson.py

def get_microphone_measurements():
    micSensor = Pin(micSensorPin, Pin.IN)         

    while(1):
        micReading = MicrophoneMeasurement(micSensor.read())
        print(micReading.decibel)


def get_mq_measurements():
    mqSensor = ADC(Pin(mqSensorPin))         
    mqSensor.atten(ADC.ATTN_11DB)   #This sets the maximum range of the sensor to 3.3v which is the input limit of the ESP32

    while(1):
        mqReading = MQMeasurement(mqSensor.read())
        print(mqReading.airQuality)
