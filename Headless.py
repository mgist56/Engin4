# Headless
# By Rowan & Meg
# ђєɭɭ๏

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# creates a lsm303 instance
lsm303 = Adafruit_LSM303.LSM303()

# pi pin configuration
RST = 24
# i2cdetect -y 1 to find adress

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# initializes library
disp.begin()

# create a blank image to draw on
# mode '1' for one bit colour
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# drawing object draws on image
draw = ImageDraw.Draw(image)

# draws a black block to clear the screen
draw.rectangle((0,0,width,height), outline=0, fill=0)

#padding makes resizing easier
padding = 2
top = padding
bottom = height-padding
x = 1

# loads the default font
font = ImageFont.load_default()

xval = []
yval = []

for i in range(26):
  xval.append(i*5)

# dimensions of screen: 64X128

while True:
  disp.display()
  time.sleep(0.5)
  disp.clear()

  accel, mag = lsm303.read()
  a, accel_y, b = accel
  mag_y = mag
  # type in the accel results
  y = round((accel_y / 10),2)
  if len(yval) > 25:
    yval.pop(0) 
  yval.append(y)
  
  draw.line((1, 1, 1, 63), fill=255)
  draw.line((1, 63, 126, 63), fill=255)
  # here are the axes
  
  if len(yval) > 1:
    if len(yval) > 25:5:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.line((1, 1, 1, 63), fill=255)
        draw.line((1, 63, 126, 63), fill=255)
    for i, d in enumerate(yval):
      if i > 0:
        x1 = xval[i]
        y1 = 64 - d
        x2 = xval[i-1]
        y2 = 64 - yval[i-1]
        print((x1, y1, x2, y2))
        print(d)
        draw.line((x1, y1, x2, y2), fill=255)

  disp.image(image)
  disp.display()