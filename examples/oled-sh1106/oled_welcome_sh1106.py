#https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico
from machine import Pin, I2C
from sh1106 import SH1106_I2C

led = Pin(25, Pin.OUT)

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
#i2c = I2C(0)
oled = SH1106_I2C(128, 64, i2c)

led.on()

oled.rotate(True)

c = 128
oled.line(0, 0, 0, 63, c)
oled.line(0, 63, 127, 63, c)
oled.line(127, 63, 127, 0, c)
oled.line(127, 0, 0, 0, c)

oled.text("Welcome to", 4, 4);
oled.text("my world!", 10, 20);

oled.show()
