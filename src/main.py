import board
import time
from adafruit_pca9685 import PCA9685

i2c = board.I2C()
pca = PCA9685(i2c)

pca.frequency = 1000

# motor channels ansteuern (die pins)
front_left_input1 = 0
front_left_input2 = 1

front_right_input1 = 2
front_right_input2 = 3

rear_left_input1 = 4
rear_left_input2 = 5

rear_rigth_input1 = 6
rear_rigth_input2 = 7

# PWM UMWANDLUNG
def pwm(speed):
    return int((abs(speed) / 100) * 65535)


# funktionen für die einzelnen Räder/Motoren
def front_left(speed):
    # invertiert
    motor(front_left_input1, front_left_input2, -speed)


def front_right(speed):
    motor(front_right_input1, front_right_input2, speed)


def rear_left(speed):
     # invertiert
    motor(rear_left_input1, rear_left_input2, -speed)


def rear_right(speed):
    motor(rear_rigth_input1, rear_rigth_input2, speed)


def stop_all():

    for i in range(8):
        pca.channels[i].duty_cycle = 0
        
        

# Motor ansteuern
def motor(input1, input2, speed):

    value = pwm(speed)

    # Vorwärts
    if speed > 0:
        pca.channels[input1].duty_cycle = value
        pca.channels[input2].duty_cycle = 0

    # Rückwärts
    elif speed < 0:
        pca.channels[input1].duty_cycle = 0
        pca.channels[input2].duty_cycle = value

    # Stop
    else:
        pca.channels[input1].duty_cycle = 0
        pca.channels[input2].duty_cycle = 0



if __name__ == "__main__":

    try:

        print("Alle Räder fahren gleichzeitig")

        front_left(40)
        front_right(40)
        rear_left(40)
        rear_right(40)

        time.sleep(1)

        stop_all()

    except KeyboardInterrupt:
        stop_all()
      