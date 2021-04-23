from machine import Pin, I2C
from sh1106 import SH1106_I2C

led = Pin(25, Pin.OUT)

#i2c = I2C(0)
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

x = 128   # 너비
y = 64    # 높이
oled = SH1106_I2C(x, y, i2c)

led.on()

# 화면 위, 아래 뒤집기
# oled.rotate(True)

# 바깥 사각형 그리기
c = 128    # 표시할 컬러 색상
oled.line(0, 0, 0, y - 1, c)
oled.line(0, y - 1, x - 1, y - 1, c)
oled.line(x - 1, y - 1, x - 1, 0, c)
oled.line(x - 1, 0, 0, 0, c)

# 환영 문구 표시
oled.text("Welcome to", 4, 4)
oled.text("my world!", 10, 20)

# 표시
oled.show()
