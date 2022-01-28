def http_post():
    import urequests
    import createMeasurementJson

    # first we access the endpoint for DHT11 sensordata
    url = "https://isensiot-api.herokuapp.com/api/createhumtemp"
    headers = {'content-type': 'application/json'}
    # measure measurements and create JSON from it
    data = createMeasurementJson.createHumTempJson()
    print(data)
    response = urequests.post(url, data=data, headers=headers)
    response.close()

    # then we access the endpoint for the microphone sensordata
    url = "https://isensiot-api.herokuapp.com/api/createmicrophone"
    headers = {'content-type': 'application/json'}
    # measure measurements and create JSON from it
    data = createMeasurementJson.createMicrophoneJson()
    print(data)
    # post the JSON
    response = urequests.post(url, data=data, headers=headers)
    response.close()




    # # first we access the endpoint for MQ sensordata
    # url = "https://isensiot-api.herokuapp.com/api/createmq135"
    # headers = {'content-type': 'application/json'}
    # # measure measurements and create JSON from it
    # data = createMeasurementJson.createMQJson()
    # print(data)
    # response = urequests.post(url, data=data, headers=headers)
    # response.close()



