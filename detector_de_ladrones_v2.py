import config
from gpiozero import LED, MotionSensor
from time import sleep
import telepot

sensor = MotionSensor(4)
alarma = LED(14)


def aviso():
	bot.sendMessage(config.id, "Ojo! Alguien ha entrado a la habitacion!")
	alarma.on()

# Start bot
bot = telepot.Bot(config.token)

while True:
	if sensor.motion_detected:
		print "Detectado movimiento"
		aviso()
		sleep(2)
		alarma.off()

