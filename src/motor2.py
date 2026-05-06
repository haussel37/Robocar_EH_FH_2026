import board
from adafruit_pca9685 import PCA9685
import json
import os

# Pfad zum aktuellen Skript ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
# Pfad zur Konfigurationsdatei zusammensetzen
config_path = os.path.join(script_dir, "config.json")

# JSON-Datei öffnen und Inhalt laden
with open(config_path, "r") as file:
    config = json.load(file)

i2c = board.I2C()
pca = PCA9685(i2c)

pca.frequency = config["frequency"]

# motor channels ansteuern (die pins)
front_left_input1 = config["channel_front_left_input1"]
front_left_input2 = config["channel_front_left_input2"]

front_right_input1 = config["channel_front_right_input1"]
front_right_input2 = config["channel_front_right_input2"]

rear_left_input1 = config["channel_rear_left_input1"]
rear_left_input2 = config["channel_rear_left_input2"]

rear_right_input1 = config["channel_rear_right_input1"]
rear_right_input2 = config["channel_rear_right_input2"]

# PWM UMWANDLUNG
def pwm(speed):
    return int((abs(speed) / config["max_speed"]) * config["max_PWM"])


# funktionen für die einzelnen Räder/Motoren
def front_left(speed):
    # invertiert
    motor(front_left_input1, front_left_input2, -speed)


def front_right(speed):
    motor(front_right_input1, front_right_input2, speed)


def rear_left(speed):
    motor(rear_left_input1, rear_left_input2, speed)


def rear_right(speed):
    # invertiert
    motor(rear_right_input1, rear_right_input2, -speed)


def stop_all():
    motor_channels = [
        front_left_input1,
        front_left_input2,
        front_right_input1,
        front_right_input2,
        rear_left_input1,
        rear_left_input2,
        rear_right_input1,
        rear_right_input2
    ]

    for channel in motor_channels:
        pca.channels[channel].duty_cycle = 0

# Motor ansteuern
def motor(input1, input2, speed):

    value = pwm(speed)

    if speed > 0:
        pca.channels[input1].duty_cycle = value
        pca.channels[input2].duty_cycle = 0

    elif speed < 0:
        pca.channels[input1].duty_cycle = 0
        pca.channels[input2].duty_cycle = value

    else:
        pca.channels[input1].duty_cycle = 0
        pca.channels[input2].duty_cycle = 0
