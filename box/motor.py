import RPi.GPIO as GPIO
import time

# explanation https://codingworld.io/project/der-servo-am-raspberry-pi 
servoPIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)

try:
	p.start(7.5)
	#while True:
	time.sleep(3)
	p.ChangeDutyCycle(12.5)
	time.sleep(1)
	#p.ChangeDutyCycle(2.5)
	#time.sleep(3)

except KeyboardInterrupt:
	print(" Terminating..")

finally:
	p.stop()
	GPIO.cleanup()
