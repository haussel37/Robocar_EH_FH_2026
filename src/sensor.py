from gpiozero import LineSensor
from time import sleep

sensor1 = LineSensor(14)
sensor2 = LineSensor(15)
sensor3 = LineSensor(23)
sensor2.when_line = lambda: print('Line detected')
sensor2.when_no_line = lambda: print('No line detected')
sleep(1)
def sensor_center():
    sensor_center.value == 1
    
def sensor_rigth():
    sensor_right.value == 1

def sensor_left():
    
