def createJson():
    import sensors as s
    import json as j

    returnableJson = ""
    # measure measurement and dump the object structure into usable JSON
    returnableJson = j.dumps(s.get_mq_measurements().__dict__)
    """print("the json returned stored in returnableJson:")
    print(returnableJson)
    print("the object in returnablejson:")

    print("--checking for JSON validity w/ jloads--")
    j.loads(returnableJson) """
    return returnableJson
