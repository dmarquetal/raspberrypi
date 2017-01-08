from gpiozero import LED
from time import sleep

led_rojo = LED(17)
led_amarillo = LED(27)
led_verde = LED(22)


while True:
	led_verde.on()
	sleep(4)
	led_verde.off()
	led_amarillo.on()
	sleep(1)
	led_amarillo.off()
	led_rojo.on()
	sleep(3)
	led_rojo.off()
