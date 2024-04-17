# Importo el código de la librería 'RPi.GPIO'
import RPi.GPIO as GPIO

# Defino los pines para los LED y el buzzer
pin_rojo = 19
pin_azul = 26
pin_verde = 13 
pin_buzzer = 22

# Configuro el modo de numeración de los pines
GPIO.setmode(GPIO.BCM)

# Configuro cada pin como una salida
GPIO.setup(pin_rojo, GPIO.OUT)
GPIO.setup(pin_azul, GPIO.OUT)
GPIO.setup(pin_verde, GPIO.OUT)
GPIO.setup(pin_buzzer, GPIO.OUT)

# Cambio el estado de encendido o apagado  de los LED
def toggle_led(led_pin):
	current_state = GPIO.input(led_pin)
	GPIO.output(led_pin, not current_state)

# Enciendo el buzzer
def buzz_on():
	GPIO.output(pin_buzzer, GPIO.HIGH)

# Apago el buzzer
def buzz_off():
	GPIO.output(pin_buzzer, GPIO.LOW)

try:
	# Creo un bucle a través del while
	while True:
		# Espero a que el usuario pueda ingresar un comando
		command = input("prompt: ")
		command_parts = command.split()

		# Verifico que el comando tenga dos partes, el comando y la opción
		if len(command_parts) == 2:
			action = command_parts[0]
			option = command_parts[1]

			#  Verifico si el comando va dirigido al buzzer
			if action == "buzz":
				if option == "on":
					buzz_on()
				elif option == "off":
					buzz_off()
				else:
					print("Opción no válida para el comando 'buzz'")

			# Verifico si el comando va dirigido al comando 'buzz'
			elif action == "rgb":
				if option == "red":
					toggle_led(pin_rojo)
				elif option == "blue":
					toggle_led(pin_azul)
				elif option == "green":
					toggle_led(pin_verde)
				else:
					print("Opción no válida para el comando 'rgb'")
			else:
				print("Comando no reconocido")
		else:
			print("Formato de comando incorrecto")

except KeyboardInterrupt:
	# Limpio los pines GPIO antes de salir
	GPIO.cleanup()
