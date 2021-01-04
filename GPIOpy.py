import RPi.GPIO as GPIO
from time import sleep

count = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while count > 0:
  GPIO.output(11, 1)
  sleep(0.5)
  GPIO.output(11, 0)
  sleep(0.5)
  count -= 1
