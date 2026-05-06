from gpiozero import LineSensor
import json
import os

# Pfad zum aktuellen Skript ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
# Pfad zur Konfigurationsdatei zusammensetzen
config_path = os.path.join(script_dir, "config.json")

# JSON-Datei öffnen und Inhalt laden
with open(config_path, "r") as file:
    config = json.load(file)

sensor_right = LineSensor(config["channel_sensor_right"])
sensor_center = LineSensor(config["channel_sensor_center"])
sensor_left = LineSensor(config["channel_sensor_left"])
