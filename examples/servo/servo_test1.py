import utime
from machine import Pin
from pico_servo import Servo

pin = Pin(15)
# 원 소스의 값 범위: minVal=2500, maxVal=7500
servo = Servo(pin, minVal=2000, maxVal=8200)    # initialize servo on GPIO pin 15

try:
    while True:
        # 0~1024 범위 사이의 값으로 서보 모터 구동
        servo.goto(0)      # 0도
        utime.sleep(1)
        servo.goto(1024)   # 180도
        utime.sleep(1)
except:
    pass

servo.free()    # 서보 모터 각도 0도

