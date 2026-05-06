from gpiozero import LineSensor
from time import sleep
import motor2

sensor1 = LineSensor(14)
sensor2 = LineSensor(15)
sensor3 = LineSensor(23)

# Sensor rechts
sensor_right = sensor1
# Sensor mitte
sensor_center = sensor2
# Sensor links
sensor_left = sensor3

def line_center_detected():
    motor2.front_left(20)
    motor2.front_right(20)
    motor2.rear_left(20)
    motor2.rear_right(20)

def line_right_detected():

    motor2.front_left(-20)
    motor2.front_right(30)
    motor2.rear_left(30)
    motor2.rear_right(-20)

def line_left_detected():
    motor2.front_left(30)
    motor2.front_right(-20)
    motor2.rear_left(-20)
    motor2.rear_right(30)
