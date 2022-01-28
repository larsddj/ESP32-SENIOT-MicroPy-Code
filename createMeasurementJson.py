def createMQJson():
    import sensors as s
    import json as j

    returnableJson = ""
    # measure measurement and dump the object structure into usable JSON
    returnableJson = j.dumps(s.get_mq_measurements().__dict__)
    return returnableJson

def createMicrophoneJson():
    import sensors as s
    import json as j

    returnableJson = ""
    # measure measurement and dump the object structure into usable JSON
    returnableJson = j.dumps(s.get_microphone_measurements_avg().__dict__)
    return returnableJson

def createHumTempJson():
    import sensors as s
    import json as j

    returnableJson = ""
    # measure measurement and dump the object structure into usable JSON
    returnableJson = j.dumps(s.get_humTemp_measurements().__dict__)
    return returnableJson