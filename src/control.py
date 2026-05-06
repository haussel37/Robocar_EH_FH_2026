import board
import time
from adafruit_pca9685 import PCA9685
import motor2
import sensor

# Sensor rechts
sensor_rechts = sensor.sensor1
# Sensor mitte
sensor_mitte = sensor.sensor2
# Sensor links
sensor_links = sensor.sensor3

def testing():
    print("snesor sensed")
    motor2.front_left(40)
    
    pass
sensor_mitte.when_line = lambda: testing
time.sleep(10000)