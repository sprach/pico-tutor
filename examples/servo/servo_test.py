import utime
from pico_servo import Servo

# 원 소스의 값 범위: minVal=2500, maxVal=7500
servo = Servo(15, minVal=2000, maxVal=8200)    # initialize servo on GPIO pin 15

angles = [0, 90, 180, 90]

try:
    while True:
        # 서보 모터 각도를 0 -> 90 -> 180 -> 90 -> 0 -> 90 -> ... 와 같이 순환해서 구동
        for angle in angles:
            servo.angleCcw(angle)
            utime.sleep(1)
except:
    pass

servo.free()    # 서보 모터 각도 0도
