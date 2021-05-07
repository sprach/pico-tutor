# 서보 모터를 PWM.duty_ns()로 구동
import time
from machine import Pin, PWM

MIN_DUTY =  500000  # 0.5ms (좌측 0도)
MAX_DUTY = 2500000  # 2.5ms (우측 180도)
MID_DUTY = int((MAX_DUTY - MIN_DUTY) / 2) + MIN_DUTY    # 1ms (중간 90도)

pwm = PWM(Pin(15))
pwm.freq(50)

def getAngleNs(angle):
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    return int( (MAX_DUTY - MIN_DUTY) / 181 * angle + MIN_DUTY )


angles = [ 0, 90, 180, 90 ]

try:
    while True:
        for angle in angles:
            print(angle)
            pwm.duty_ns(getAngleNs(angle))
            time.sleep(1)

except:
    pass

# 0도
print(0)
pwm.duty_ns(getAngle2Ns(0))
