from gpiozero import LED, MotionSensor
from time import sleep

sensor = MotionSensor(4)
alarma = LED(14)

while True:
	if sensor.motion_detected:
		print "Detectado movimiento"
		alarma.on()
		sleep(2)
		alarma.off()

