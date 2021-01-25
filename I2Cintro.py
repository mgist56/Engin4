# I2C Intro
# By Rowan & Meg
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Raspberry Pi pin configuration:
RST = 24
# DC = 23
# SPI_PORT = 0
# SPI_DEVICE = 0
# find your address by typing i2cdetect -y 1

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = 2
top = padding
bottom = height-padding
x = 1

# Load default font.
font = ImageFont.load_default()

while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    # type in the accel results
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    draw.text((x, top),'Accel X={0}, Y={1}, Z={2}'.format(accel_x, accel_y, accel_z), font=font, fill=255)
    draw.text((x, top+5),'Mag X={0}, Y={1}, Z={2}'.format(mag_x, mag_y, mag_z), font=font, fill=255)
    # Wait half a second and repeat.
    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(0.5)
    disp.clear()
