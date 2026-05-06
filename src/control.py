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
speed = 20
def line_detected():
    motor2.front_left(speed)
    motor2.front_right(speed)
    motor2.rear_left(speed)
    motor2.rear_right(speed)

while True:


# Linie schwarz erkennt -> Motor an
    if sensor_center.value ==1:
        line_detected()

# Linie weiß erkennt -> Motor Stop
    else:
        motor2.stop_all()
