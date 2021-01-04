import RPi.GPIO as GPIO
from time import sleep

count = 10
#the counter! declared simply!!
GPIO.setmode(GPIO.BOARD)
#setmode needed before setup
GPIO.setup(11, GPIO.OUT)
#numb 11 for pin 17 on the pi

while count > 0:
  #LEDs blinks 10 times
  GPIO.output(11, 1)
  sleep(0.5)
  GPIO.output(11, 0)
  sleep(0.5)
  count -= 1
#py is so much better than bash
#it really is
