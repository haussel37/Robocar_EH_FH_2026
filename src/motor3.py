import motor2
import time
import board
from adafruit_pca9685 import PCA9685


motor2.front_left(30)
motor2.front_right(30)
motor2.rear_left(30)
motor2.rear_right(30)

time.sleep(1)

motor2.stop_all()
