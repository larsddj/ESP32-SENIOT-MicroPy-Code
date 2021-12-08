def http_post():
    import urequests
    import createMeasurementJson
    # data specific to our endpoints
    url = "https://isensiot-api.herokuapp.com/api/createmq135"
    headers = {'content-type': 'application/json'}
    # measure measurements and create JSON from it
    data = createMeasurementJson.createJson()
    # post the JSON
    urequests.post(url, data=data, headers=headers)

