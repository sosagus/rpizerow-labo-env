## Importo los paquetes de código de las librerías "gpiozero" y "time"
from gpiozero import LED
from time import sleep

## Asigno a los tres colores del LED sus respectivos pines.
rojo = LED(19)
verde = LED(13)
azul = LED(26)

## Ejecuto un bucle a través de un while para que los LEDs parpadeen cada cierto tiempo, con cada uno "pisándose" y mezclando los colores
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
