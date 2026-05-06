# Linienfolgender Roboter
## Projektbeschreibung

Dieses Projekt realisiert einen autonomen Linienfolger-Roboter auf Basis eines Raspberry Pi.

Der Roboter erkennt mit drei Liniensensoren eine schwarze Linie auf hellem Untergrund und steuert vier Gleichstrommotoren entsprechend an. Die Fahrsteuerung erfolgt durch eine einfache regelbasierte Bang-Bang-Steuerung ohne PID-Regler.

Die Sensorwerte werden kontinuierlich ausgewertet, um die Fahrtrichtung anzupassen und die Linie zu verfolgen.

## Bang-Bang-Steuerung
Der Linienfolger verwendet eine sogenannte Bang-Bang-Steuerung.

Bei dieser Steuerungsart gibt es keine stufenlose Regelung der Motorgeschwindigkeit. Stattdessen werden feste Fahrbefehle abhängig von den Sensorzuständen ausgeführt.

Die Steuerung kennt nur wenige Zustände:

- Geradeaus fahren
- Nach links korrigieren
- Nach rechts korrigieren
- Linie suchen

Sobald ein Sensor die Linie erkennt, wird sofort die zugehörige Aktion ausgeführt. Die Motoren wechseln dabei direkt zwischen den vorgegebenen Zuständen, ohne Zwischenwerte zu berechnen.

Vorteile:
- Einfache Implementierung
- Geringer Rechenaufwand
- Gut geeignet für einfache Linienfolger

Nachteile:
- Unruhigeres Fahrverhalten
- Geringere Genauigkeit in Kurven
- Keine automatische Anpassung an unterschiedliche Geschwindigkeiten

Im Gegensatz zu einem PID-Regler berücksichtigt die Bang-Bang-Steuerung nur den aktuellen Sensorzustand und nicht die Stärke oder Dauer einer Abweichung von der Linie.

## Verwendete Hardware
- Raspberry Pi
- PCA9685 PWM-Modul
- 3 Liniensensoren
- 4 DC-Motoren
- Motortreiber
- Externe Spannungsversorgung
- I²C-Verbindung


## Softwareaufbau
### main.py

Startpunkt des Programms.

#### Aufgabe:
- Importiert die Steuerlogik
- Startet das Hauptprogramm
```python
import control

control.control_run()
```

### control.py
Enthält die Fahrlogik des Roboters.

#### Funktionen:
- Geradeaus fahren
- Nach links korrigieren
- Nach rechts korrigieren
- Linie suchen
- Sensorwerte auswerten

### sensor.py
Verwaltet die Liniensensoren.

#### Aufgaben:
- Initialisierung der Sensoren
- Bereitstellung der Sensorzustände

#### Verwendete Sensoren:
| Sensor | Position |
|---------|----------|
| sensor_left | links |
| sensor_center | mitte |
| sensor_right | rechts |

### motor2.py
Steuert die vier Motoren über das PCA9685-Modul.

#### Aufgaben:
- Initialisierung des PWM-Moduls
- Ansteuerung einzelner Motoren
- Geschwindigkeitsregelung
- Stoppen aller Motoren

### config.json
Enthält zentrale Konfigurationsparameter.

#### Beispiele:

```json
{
  "speed_straight": 25,
  "speed_forward": 30,
  "speed_back": -15
}
```

#### Vorteile:
- Keine Magic Numbers im Quellcode
- Einfache Anpassung der Geschwindigkeiten
- Zentrale Verwaltung aller Parameter

## Funktionsweise
Der Roboter verwendet drei Liniensensoren.

### Geradeausfahrt
Wenn der mittlere Sensor die Linie erkennt:

`0 1 0`

fährt der Roboter geradeaus.

### Linkskorrektur
Wenn der rechte Sensor die Linie erkennt:

`0 0 1`

lenkt der Roboter nach links.

### Rechtskorrektur
Wenn der linke Sensor die Linie erkennt:

`1 0 0`

lenkt der Roboter nach rechts.

### Linienverlust
Wenn kein Sensor die Linie erkennt:

`0 0 0`

sucht der Roboter die Linie anhand der zuletzt bekannten Position.

## Projektstruktur

```text
.
├── main.py
├── control.py
├── motor2.py
├── sensor.py
├── config.json
└── README.md
```

## Installation
Benötigte Bibliotheken installieren:
```bash
python3 -m pip install gpiozero
python3 -m pip install adafruit-circuitpython-pca9685
python3 -m pip install adafruit-blinka
```
## Programm starten
```bash
python3 main.py
```
## Programm beenden
`STRG + C`

Beim Beenden werden alle Motoren gestoppt.

## Mögliche Erweiterungen
- PID-Regler
- Geschwindigkeitsregelung über Encoder
- Kreuzungserkennung
- Hinderniserkennung
- WLAN-Fernsteuerung


## Autor

- Ellen Haußmann
- Felix Haußmann

Studiengang: TMT 2025

Projekt: Linienfolgender Roboter mit Raspberry Pi

Jahr: 2026
