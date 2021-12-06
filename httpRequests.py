def http_post():
    import urequests
    import createMeasurementJson
    url = "https://isensiot-api.herokuapp.com/api/createmq135"
    headers = {'content-type': 'application/json'}
    data = createMeasurementJson.createJson()
    print (data)
    urequests.post(url, data=data, headers=headers)
    #JSON dump our sensor data here
