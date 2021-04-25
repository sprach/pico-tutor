"""
루프에 의한 LED 깜빡임
- 프로세스 점유
"""
from machine import Pin
import time

led = Pin(25, Pin.OUT)    # 내장 GP25

while True:
    # 방법 1
    # led.on()
    # time.sleep(1)
    # led.off()
    # time.sleep(1)

    # 방법 2
    led.toggle()
    time.sleep(1)
