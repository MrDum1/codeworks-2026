from gpiozero import LED
from time import sleep

Red_led = LED(18)
Yellow_led = LED(17)
Green_led = LED(15)

while True:
	Green_led.off()
	Red_led.on()
	sleep(3)
	Red_led.off()
	Yellow_led.on()
	sleep(1)
	Yellow_led.off()
	Green_led.on()
	sleep(3)
