# Headless
# By Rowan & Meg
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

x_values = []
y_values = []
points = []

for i in range(26):
  x_values.append(i*5)

33.125

while True:


    print(points)
    disp.display()
    time.sleep(0.5)
    disp.clear()
    
    accel, mag = lsm303.read()
    a, accel_y, b = accel
    mag_y = mag
    # type in the accel results
    y = round((accel_y / 33),2)
    y_values.append(y)
    
    points.append([])
    # draw.line((1,y,128,y), fill=255
    draw.line((1, 1, 1, 64), fill=255)
    draw.line((1, 63, 126, 63), fill=255)
    # add second draw.line to pi
      
  for d in y_values:
    draw.line(x_values[index(d)], y_values[index(d)], x_values[index(d)+1],)

    disp.image(image)
    # disp.display() is needeed here

    # ImageDraw.line(points, fill=None, width=1, joint=None)
    # syntax to draw a line
