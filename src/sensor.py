from gpiozero import LineSensor
from time import sleep

sensor = LineSensor(14)
sensor = LineSensor(15)
sensor = LineSensor(23)
sensor.when_line = lambda: print('Line detected')
sensor.when_no_line = lambda: print('No line detected')
sleep(10000)