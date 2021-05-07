import utime
from pico_servo import Servo

# 원 소스의 값 범위: minVal=2500, maxVal=7500
servo = Servo(15, minVal=2000, maxVal=8200)    # initialize servo on GPIO pin 15

try:
    while True:
        # angle(Ccw) 값으로 서보 모터 구동
        servo.angleCcw(0)
        utime.sleep(1)
        servo.angleCcw(90)
        utime.sleep(1)
        servo.angleCcw(180)
        utime.sleep(1)
        servo.angleCcw(0)
        utime.sleep(1)
        servo.angleCcw(90)
        utime.sleep(1)
except:
    pass

servo.free()    # 서보 모터 각도 0도

