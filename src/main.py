from gpiozero import Buzzer
from time import sleep

bz = Buzzer(17)
bz.off()
sleep(1)