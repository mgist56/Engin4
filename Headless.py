# Headless
# By Rowan & Meg

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# dimensions of the screen: 64X128

# creates an lsm303 instance
lsm303 = Adafruit_LSM303.LSM303()

# pi pin configuration
RST = 24
# i2cdetect -y 1 to find the adress
# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
# initializes library
disp.begin()

# create a blank image to draw on
# mode '1' for one bit colour
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
# black rectangle can be used to clear the screen
draw.rectangle((0,0,width,height), outline=0, fill=0)
# padding makes resizing easier
padding = 2
top = padding
bottom = height-padding
x = 1
# loads the default font
font = ImageFont.load_default()

# originally we used one list
# but it's a lot easier to use two
xval = []
yval = []

for i in range(26):
  # this creates the right number of
  # elements for the x values list
  xval.append(i*5)

while True:
  disp.display()
  time.sleep(0.5)
  disp.clear()

  accel, mag = lsm303.read()
  a, accel_y, b = accel
  mag_y = mag
  # rounding by ten makes the scale on the
  # screen more mangiable and easier to see
  y = round((accel_y / 10),2)
  
  # 25 spaces are the total number of
  # spaces that the y value array should hold
  if len(yval) > 25:
    # "pop" removes the last element on the list
    yval.pop(0)
  yval.append(y)

  # this creates the axes for the graph
  draw.line((1, 1, 1, 63), fill=255)
  draw.line((1, 63, 126, 63), fill=255)
  
  if len(yval) > 1:
    if len(yval) > 25:
        # the axes need to be redrawn each time that the
        # new data loops in order for things to not overlap
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.line((1, 1, 1, 63), fill=255)
        draw.line((1, 63, 126, 63), fill=255)
    # i and d are the number of elements in the y array    
    for i, d in enumerate(yval):
      if i > 0:
        x1 = xval[i]
        # since the screen is flipped, the y data needs to be
        #subtracted from 64 (the total height of the screen) so
        # that the points are not at the top of the screen
        y1 = 64 - d
        x2 = xval[i-1]
        y2 = 64 - yval[i-1]
        # this shows the points to make it easier
        # to see bad data and fix issues
        print((x1, y1, x2, y2))
        print(d)
        draw.line((x1, y1, x2, y2), fill=255)

  disp.image(image)
  disp.display()