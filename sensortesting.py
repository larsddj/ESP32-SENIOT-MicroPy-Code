import time
from time import sleep
from machine import Pin, ADC
import dht 
from measurements import MQMeasurement, MicrophoneMeasurement, HumidTempMeasurement

mqSensorPin = 18 # the GPIO pin the MQ-135 sensor is plugged into on the ESP32
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

#testing method for the dht11 sensor
def get_dht11_measurements():
    sensor = dht.DHT11(Pin(14))

    while(1):
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)

#method to compare multiple dht11's for calibration purposes
def compare_dht11_measurements():
    sensor = dht.DHT11(Pin(14))
    sensor2 = dht.DHT11(Pin(27))

    while(1):
        sleep(2)
        sensor.measure()
        sensor2.measure()
        temp = sensor.temperature()
        temp2 = sensor2.temperature()
        hum = sensor.humidity()
        hum2 = sensor2.humidity()
        temp_f = temp * (9/5) + 32.0
        temp_f2 = temp2 * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
        print('Temperature 2: %3.1f C' %temp2)
        print('Temperature 2: %3.1f F' %temp_f2)
        print('Humidity 2: %3.1f %%' %hum2)