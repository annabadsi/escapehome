import RPi.GPIO as GPIO
import time


pin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
	state = GPIO.input(pin)
	while True:
		if GPIO.input(pin) != state:
			state = GPIO.input(pin)
			if state == 1:
				print "it's open!"
			else:
				print "closed"
		time.sleep(1)
except KeyboardInterrupt:
	print(" Terminating..")
finally:
	GPIO.cleanup()
