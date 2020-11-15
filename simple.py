# Imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Pins
SENSOR_1 = 7

"""
Using LN298N motor drive to control the pumps

    Pump A : IN1 and IN2.  On: 1 and 0, Off: 0 and 0. (Enable1 High)

"""

IN1 = 11
GPIO.setup(IN1, GPIO.OUT)

GPIO.setup(SENSOR_1, GPIO.IN)


# The following is a function to read the sensor value which takes the pin number as input and returns 1 if dry and 0 if wet
def read_sensor(pin):
    reading = GPIO.input(pin)
    print("Sensor reading is: ", reading)
    return reading

# Turns the pump<PinNumber> on 
def turn_pump_on(pumpPinNo):
    print("Motor is turned on.")
    GPIO.output(pumpPinNo, 1)

# Turns the pump<Number> off 
def turn_pump_off(pumpPinNo):
    print("Motor is turned off.")
    GPIO.output(pumpPinNo, 0)

plants = [SENSOR_1]
pumps = [IN1]

def check_status(plants):
    status = []
    for plant in plants:
        status.append(read_sensor(plant))
    return status        

sleepTime = 5

# Infinite Loop
while True:
    print("Checking status of the plants.......")
    status = check_status(plants)
    for i in range(0,len(status)):
        if status[i] == 1:      # the plant is dry!
            print("Dry plant found: ", plants[i])
            turn_pump_on(pumps[i])
            while read_sensor(plants[i]) == 1:
                #do nothing and wait
                #pass
                time.sleep(1)
            turn_pump_off(pumps[i])
            print("I just watered the plant: ",  plants[i])

    print("Will check the status of the plants again in ", sleepTime)
    print("")
    time.sleep(sleepTime)



