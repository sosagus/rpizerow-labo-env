## Importo los paquetes de código de las librerías "gpiozero" y "signal"
from gpiozero import LED, Button
from signal import pause

## Asigno al LED y al pulsador sus respectivos pines
led = LED (19)
button = Button(18)

## Ejecuto el comando para que, cuando presione el pulsador, el LED se encienda, y cuando no lo haga este se apague.
button.when_pressed = led.on
button.when_released = led.off

pause()
