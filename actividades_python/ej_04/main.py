# Importa las liberías que se van a usar
from gpiozero import PWMLED
import ADS1x15
import time
import math

# Configuración del ADC
ADS = ADS1x15.ADS1115(1,0x48)
ADS.setMode(ADS.MODE_SINGLE)
ADS.setGain(ADS.PGA_4_096V)
factor = ADS.toVoltage()

# Declara qué pines PWMLED son de los LED azul y rojo.
ledB = PWMLED(26)
ledR = PWMLED(19)

# Lista de las variables referidas a la temperatura
VCC = 3.3
R = 10000
beta = 3900
t0 = 298.15
t = 0
rt = 0

while True:
    # Lectura de los valores analógicos obtenidos
    LecturaPote = ADS.readADC(3)
    LecturaTerm = ADS.readADC(1)

    # Conversión a voltaje
    LecturaPoteVoltaje = LecturaPote * factor
    LecturaTermVoltaje = LecturaTerm * factor

    # Calcular la resistencia del termistor
    rt = (R * LecturaTermVoltaje) / (VCC - LecturaTermVoltaje)

    # Conversión a temperatura en °C
    t = beta / (math.log(rt / R) + (beta / t0))
    t = t - 273.15

    # Escalar el voltaje en un rango de entre 0-30°C
    TempPote = (LecturaPoteVoltaje / 3.3) * 30

    # Calculo de diferencia entre la temperatura deseada y la medida
    diff = abs(TempPote - t)

    # Limitar la diferencia a un máximo de 5°C
    if diff > 5:
        diff = 5

    # Control de potencia de los LEDS
    if TempPote > t:
        ledB.value = 0
        ledR.value = diff / 5
    elif TempPote < t:
        ledB.value = diff / 5
        ledR.value = 0
    else:
        ledB.value = 0
        ledR.value = 0

    # Muestra los valores obtenidos
    print("Termistor: {0:.3f} V, {1:.3f} °C".format(LecturaTermVoltaje, t))
    print("Potenciómetro: {0:.2f} °C".format(TempPote))

    time.sleep(1)
