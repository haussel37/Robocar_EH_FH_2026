import board
from time import sleep
from adafruit_pca9685 import PCA9685
import motor2
import sensor

# Sensoren
sensor_right = sensor.sensor_right
sensor_center = sensor.sensor_center
sensor_left = sensor.sensor_left

speed = 20
speed_1 = 30
speed_2 = -15

last_seen_line = "sensor_mitte"

def control_run():
    while True:
        right = sensor_right.value
        center = sensor_center.value
        left = sensor_left.value

        if center == 1:
            last_seen_line = "sensor_mitte"
        # geradeaus fahren
            motor2.front_left(speed)
            motor2.front_right(speed)
            motor2.rear_left(speed)
            motor2.rear_right(speed)

        elif right == 1:
            last_seen_line = "sensor_rechts"
        # nach rechts lenken
            motor2.front_left(speed_2)
            motor2.front_right(speed_1)
            motor2.rear_left(speed_2)
            motor2.rear_right(speed_1)


        elif left == 1:
            last_seen_line = "sensor_links"
            # nach links lenken
            motor2.front_left(speed_1)
            motor2.front_right(speed_2)
            motor2.rear_left(speed_1)
            motor2.rear_right(speed_2)

        else:
            # keine Linie erkannt -> in letzter Richtung suchen
            if last_seen_line == "sensor_rechts":
                motor2.front_left(speed_2)
                motor2.front_right(speed_1)
                motor2.rear_left(speed_2)
                motor2.rear_right(speed_1)


            elif last_seen_line == "sensor_links":
                motor2.front_left(speed_1)
                motor2.front_right(speed_2)
                motor2.rear_left(speed_1)
                motor2.rear_right(speed_2)

            else:
                # wenn nicht sensor rechts oder senosr links erkannt wurde
                motor2.front_left(speed)
                motor2.front_right(speed)
                motor2.rear_left(speed)
                motor2.rear_right(speed)

        sleep(0.05)
