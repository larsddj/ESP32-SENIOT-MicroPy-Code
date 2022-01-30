import time
from time import sleep
from machine import Pin, ADC
import dht 
from measurements import MQMeasurement, MicrophoneMeasurement, HumidTempMeasurement

mqSensorPin = 18 # the GPIO pin the MQ-135 sensor is plugged into on the ESP32
micSensorPin = 34 # the GPIO pin the microphone sensor is plugged into on the ESP32

# these sensor methods retrieve measurements from a sensor and attach a timestamp object
# these measurements and timestamps are used for JSON serialization in createMeasurementJson.py


# because our sensor has quite a lot of jitter we need to account for it
# we can do this by taking a large sample of data, averaging it out and seeing if the average is above a given threshold
def get_microphone_measurements():
    micSensor = Pin(micSensorPin, Pin.IN)         
    i = 0
    micMeasurements = [] 
    while(i<5000):
        value = micSensor.value()
        micMeasurements.append(value)
        print(value)
        i+=1

    total = 0
    for x in micMeasurements:
        total+=x
    
    print(total)
    average = total/5000
    print(average)

def get_microphone_measurement_collumn_1mswait():
    micSensor = Pin(micSensorPin, Pin.IN)         
    i = 0
    micMeasurements = [] 
    while(i<5000):
        value = micSensor.value()
        micMeasurements.append(value)
        print(value)
        sleep(0.001)
        i+=1

    total = 0
    for x in micMeasurements:
        total+=x
    
    print(total)
    average = total/5000
    print(average)
    


def get_mq_measurements():
    mqSensor = ADC(Pin(mqSensorPin))         
    mqSensor.atten(ADC.ATTN_11DB)   #This sets the maximum range of the sensor to 3.3v which is the input limit of the ESP32

    while(1):
        mqReading = MQMeasurement(mqSensor.read())
        print(mqReading.airQuality)

#testing method for the dht11 sensor
def get_dht11_measurements():
    sensor = dht.DHT11(Pin(4))

    while(1):
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)

#method for getting dht11 calibration data
def get_dht11_measurements_collumn_1secwait():
    sensor = dht.DHT11(Pin(4))

    while(1):
        sleep(1)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(str(temp)+"\t"+str(hum))

#method to compare multiple dht11's for calibration purposes
def compare_dht11_measurements_collumn_2secwait():
    sensor = dht.DHT11(Pin(4))
    sensor2 = dht.DHT11(Pin(2))
    dht1Measurements = [] 
    dht2Measurements = [] 

    i=0
    while(i < 100):
        sleep(2)
        sensor.measure()
        sensor2.measure()
        temp = sensor.temperature()
        temp2 = sensor2.temperature()
        hum = sensor.humidity()
        hum2 = sensor2.humidity()
        dht1Measurements.append(str(temp)+"\t"+str(hum))
        dht2Measurements.append(str(temp2)+"\t"+str(hum2))
        i+=1
    
    print("----------!NOW PRINTING DHT11 1 MEASUREMENTS! (TEMP CELSIUS - HUMIDITY)---------------")
    for dhtMeasurementString in dht1Measurements:
        print(dhtMeasurementString)
    
    print("----------!NOW PRINTING DHT11 2 MEASUREMENTS! (TEMP CELSIUS - HUMIDITY)---------------")
    for dhtMeasurementString in dht2Measurements:
        print(dhtMeasurementString)