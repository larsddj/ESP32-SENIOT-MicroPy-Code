def createJson():
    import sensors as s
    import json as j

    returnableJson = ""
    print(s.get_microphone_measurements())
    returnableJson = j.dumps(s.get_microphone_measurements())
    print(returnableJson)

    j.loads(returnableJson)
    return returnableJson
