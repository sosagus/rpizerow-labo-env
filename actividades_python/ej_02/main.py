from gpiozero import LED
from time import sleep

rojo = LED(19)
verde = LED(13)
azul = LED(26)

while True:
	verde.on()
	sleep(0.25)
	azul.off()

	rojo.on()
	sleep(1)
	verde.off()

	azul.on()
	sleep(0.5)
	rojo.off()
