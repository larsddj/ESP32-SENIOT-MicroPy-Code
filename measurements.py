class MQMeasurement:
    def __init__(self,NH3,NO2,Alcohol,Benzene,Smoke,CO2):
        self.NH3 = NH3
        self.NO2 = NO2
        self.Alchohol = Alcohol
        self.Benzene = Benzene
        self.Smoke = Smoke
        self.CO2 = CO2
        self.timeSpentMs = 0

    def setTimeSpent(self, timeSpentMs):
        self.timeSpentMs = timeSpentMs

class MicrophoneMeasurement:
    def __init__(self,db):
        self.db = db
        self.timeSpentMs = 0

    def setTimeSpent(self, timeSpentMs):
        self.timeSpentMs = timeSpentMs

class HumidTempMeasurement:
    def __init__(self,humidity, temperature):
        self.humidity = humidity
        self.temperature = temperature
        self.timeSpentMs = 0

    def setTimeSpent(self, timeSpentMs):
        self.timeSpentMs = timeSpentMs