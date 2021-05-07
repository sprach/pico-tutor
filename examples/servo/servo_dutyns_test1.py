# 서보 모터를 PWM.duty_ns()로 구동
import time
from machine import Pin, PWM

MIN_DUTY =  500000  # 0.5ms (좌측 0도)
MAX_DUTY = 2500000  # 2.5ms (우측 180도)
MID_DUTY = int((MAX_DUTY - MIN_DUTY) / 2) + MIN_DUTY    # 1ms (중간 90도)

pwm = PWM(Pin(15))
pwm.freq(50)

try:
	while True:
		# 0도
		print(MIN_DUTY)
		pwm.duty_ns(MIN_DUTY)
		time.sleep(1)

		# 90도
		print(MID_DUTY)
		pwm.duty_ns(MID_DUTY)
		time.sleep(1)

		# 180도
		print(MAX_DUTY)
		pwm.duty_ns(MAX_DUTY)
		time.sleep(1)

		# 90도
		print(MID_DUTY)
		pwm.duty_ns(MID_DUTY)
		time.sleep(1)

except:
	pass

# 0도
print(MIN_DUTY)
pwm.duty_ns(MIN_DUTY)
