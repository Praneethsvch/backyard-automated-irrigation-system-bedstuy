# Imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Pins
SENSOR_1 = 7

GPIO.setup(SENSOR_1, GPIO.IN)

def read_sensor(pin):
    reading = GPIO.input(pin)
    print("Sensor Reading is: ", reading)
    return reading

# Infinite Loop
while True:
    reading = read_sensor(SENSOR_1)
    time.sleep(2)



