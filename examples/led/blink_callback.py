"""
콜백에 의한 LED 깜빡임
- 프로세스 미점유
"""
from machine import Pin, Timer

led = Pin(25, Pin.OUT)    # 내장 GP25
timer = Timer()


# timer 인수는 내부 호출되니 생략하면 안됨
def blink(timer):
    led.toggle()


# freq: 주파수
# n초 = 1 / freq
timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)