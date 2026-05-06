import board
from time import sleep
from adafruit_pca9685 import PCA9685
import motor2
import sensor
import random

# Sensoren
sensor_right = sensor.sensor_right
sensor_center = sensor.sensor_center
sensor_left = sensor.sensor_left

speed = 20
speed_1 = 30
speed_2 = -15

#Variable zuordnen
last_seen_line = "sensor_mitte"

def drive_straight():
    motor2.front_left(speed)
    motor2.front_right(speed)
    motor2.rear_left(speed)
    motor2.rear_right(speed)

def turn_right():
    motor2.front_left(speed_2)
    motor2.front_right(speed_1)
    motor2.rear_left(speed_2)
    motor2.rear_right(speed_1)

def turn_left():
    motor2.front_left(speed_1)
    motor2.front_right(speed_2)
    motor2.rear_left(speed_1)
    motor2.rear_right(speed_2)

def control_run_2():
    #wissen das last_seen_line eine veränderliche variable ist
    global last_seen_line
    while True:
        # Kreuzung zufällig wählen ob rechts oder links fahren
        if sensor_left.value == 1 and sensor_right.value == 1 and sensor_center.value == 1:
            motor2.stop_all()
            sleep(1)

            direction = random.choice(["turn_left","turn_right"])

            if direction == "turn_left":
                turn_left()
                sleep(0.5)

            else :
                turn_right()
                sleep(0.5
                )
        # wenn kein Sensor eine Linie sehen, dann die motoren stoppen
       # elif sensor_left.value == 0 and sensor_right.value == 0 and sensor_center.value == 0:
            #motor2.stop_all()

        elif sensor_center.value == 1:
            drive_straight()
            #Variable zuordnen
            last_seen_line = "sensor_mitte"

        elif sensor_right.value == 1:
            turn_right()
            #Variable zuordnen
            last_seen_line = "sensor_rechts"


        elif sensor_left.value == 1:
            turn_left()
            #Variable zuordnen
            last_seen_line = "sensor_links"

        else:
            # keine Linie erkannt -> in letzter Richtung suchen/fahren
            if last_seen_line == "sensor_rechts":
                turn_right()


            elif last_seen_line == "sensor_links":
                turn_left()

            else:
                # last_seen_line == "sensor_mitte"
                drive_straight()

        sleep(0.05)

control_run_2()


import board
from time import sleep
from adafruit_pca9685 import PCA9685
import motor2
import sensor

# Sensoren
sensor_right = sensor.sensor_right
sensor_center = sensor.sensor_center
sensor_left = sensor.sensor_left


speed_straight = 20
speed_forward = 20
speed_back = -20

black_line = 1

#Variable zuordnen
last_seen_line = "sensor_mitte"

def control_run():
    try:
        global last_seen_line
        while True:
            if sensor_center.value == black_line:
                motor2.front_left(speed_straight)
                motor2.front_right(speed_straight)
                motor2.rear_left(speed_straight)
                motor2.rear_right(speed_straight)
                #Variable neu zuordnen
                last_seen_line = "sensor_mitte"

            elif sensor_right.value == black_line:
                motor2.front_left(speed_back)
                motor2.front_right(speed_forward)
                motor2.rear_left(speed_back)
                motor2.rear_right(speed_forward)
                #Variable neu zuordnen
                last_seen_line = "sensor_rechts"


            elif sensor_left.value == black_line:
                motor2.front_left(speed_forward)
                motor2.front_right(speed_back)
                motor2.rear_left(speed_forward)
                motor2.rear_right(speed_back)
                #Variable neu zuordnen
                last_seen_line = "sensor_links"

            else:
                # keine Linie erkannt -> in letzter Richtung suchen
                if last_seen_line == "sensor_rechts":
                    motor2.front_left(speed_back)
                    motor2.front_right(speed_forward)
                    motor2.rear_left(speed_back)
                    motor2.rear_right(speed_forward)


                elif last_seen_line == "sensor_links":
                    motor2.front_left(speed_forward)
                    motor2.front_right(speed_back)
                    motor2.rear_left(speed_forward)
                    motor2.rear_right(speed_back)

                else:
                    # last_seen_line == "sensor_mitte"
                    motor2.front_left(speed_straight)
                    motor2.front_right(speed_straight)
                    motor2.rear_left(speed_straight)
                    motor2.rear_right(speed_straight)

            sleep(0.05)
    except KeyboardInterrupt:
        motor2.stop_all()
