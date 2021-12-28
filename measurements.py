class MQMeasurement:
    def __init__(self,Airquality):
        self.Airquality = Airquality
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