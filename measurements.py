class MQMeasurement:
    def __init__(self,nh3,no2,alcohol,benzene,smoke,co2):
        self.nh3 = nh3
        self.no2 = no2
        self.alchohol = alcohol
        self.benzene = benzene
        self.smoke = smoke
        self.co2 = co2
        self.timeSpent = 0

    def setTimeSpent(self, timeSpent):
        self.timeSpent = timeSpent

class MicrophoneMeasurement:
    def __init__(self,db):
        self.db = db
        self.timeSpent = 0

    def setTimeSpent(self, timeSpent):
        self.timeSpent = timeSpent

class HumidTempMeasurement:
    def __init__(self,humidity, temperature):
        self.humidity = humidity
        self.temperature = temperature
        self.timeSpent = 0

    def setTimeSpent(self, timeSpent):
        self.timeSpent = timeSpent