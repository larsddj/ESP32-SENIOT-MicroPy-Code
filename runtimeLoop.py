import httpRequests as api

# this file executes the runtime loop of the sensor
# from here we call the processes needed to do routine behaviour
# after the routine behaviour is finished we enter sleep for a certain amount of time

def deep_sleep(msAmount):
    # machine's system clock
    rtc = machine.RTC()
    # create the irq object that will trigger from ALARM0; here we wake from deep sleep
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    # fire off the alarm after msAmount of milliseconds
    rtc.alarm(rtc.ALARM0, msAmount)
    # put the device to sleep
    machine.deepsleep()

# our default execution cycle
def runtimeExecution():
    # post our measurements TO-DO: change structure a bit, this currently fires off everything
    api.http_post()

    # temporary sleep to ensure we can catch our device awake
    sleep(5)

    # finally we enter our deep sleep state; rebooting the whole process on wakeup
    deep_sleep(10000)
