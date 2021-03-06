class MQMeasurement:
    def __init__(self,airQuality):
        self.airQuality = airQuality
        self.timeSpentMs = 0

    def setTimeSpent(self, timeSpentMs):
        self.timeSpentMs = timeSpentMs

class MicrophoneMeasurement:
    def __init__(self,soundPollution):
        self.soundPollution = soundPollution
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