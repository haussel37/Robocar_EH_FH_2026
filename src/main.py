import board
from time import sleep
from adafruit_pca9685 import PCA9685
import motor2
import sensor



# Sensor rechts
sensor_right = sensor.sensor1
# Sensor mitte
sensor_center = sensor.sensor2
# Sensor links
sensor_left = sensor.sensor3

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

while True:
    if sensor_center.value ==1:
        line_center_detected()

    elif sensor_right.value ==1:
        line_right_detected()


    elif sensor_left.value ==1:
        line_left_detected()


    elif (sensor_center.value ==0
        and sensor_right.value ==0
        and sensor_left.value ==0):
            motor2.stop_all()
    sleep(0.01)
