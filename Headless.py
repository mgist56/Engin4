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

while True:
    disp.display()
    time.sleep(0.5)
    disp.clear()
    # read X, Y, Z values and print them
    accel, mag = lsm303.read()
    accel_y = accel
    mag_y = mag
    # type in the accel results
    
    # draw a black box to prevent overlap
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    

    disp.image(image)
    # disp.display() is needeed here
