from time import sleep
import motor2
import sensor
import json
import os

# Pfad zum aktuellen Skript ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
# Pfad zur Konfigurationsdatei zusammensetzen
config_path = os.path.join(script_dir, "config.json")

# JSON-Datei öffnen und Inhalt laden
with open(config_path, "r") as file:
    config = json.load(file)

# Sensoren
sensor_right = sensor.sensor_right
sensor_center = sensor.sensor_center
sensor_left = sensor.sensor_left

def drive_straight():
    motor2.front_left(config["speed_straight"])
    motor2.front_right(config["speed_straight"])
    motor2.rear_left(config["speed_straight"])
    motor2.rear_right(config["speed_straight"])

def turn_right():
    motor2.front_left(config["speed_back"])
    motor2.front_right(config["speed_forward"])
    motor2.rear_left(config["speed_back"])
    motor2.rear_right(config["speed_forward"])

def turn_left():
    motor2.front_left(config["speed_forward"])
    motor2.front_right(config["speed_back"])
    motor2.rear_left(config["speed_forward"])
    motor2.rear_right(config["speed_back"])


# Variable zuordnen
last_seen_line = "sensor_center"

def control_run():
    try:
        global last_seen_line
        while True:
            if sensor_center.value == config["black_line"]:
                drive_straight()
                # Variable neu zuordnen
                last_seen_line = "sensor_center"

            elif sensor_right.value == config["black_line"]:
                turn_right()
                # Variable neu zuordnen
                last_seen_line = "sensor_right"


            elif sensor_left.value == config["black_line"]:
                turn_left()
                # Variable neu zuordnen
                last_seen_line = "sensor_left"

            else:
                # keine Linie erkannt -> in letzter Richtung suchen
                if last_seen_line == "sensor_right":
                    turn_right()


                elif last_seen_line == "sensor_left":
                    turn_left()

                else:
                    # last_seen_line == "sensor_center"
                    drive_straight()

            sleep(config["time_loop"])
    except KeyboardInterrupt:
        motor2.stop_all()
