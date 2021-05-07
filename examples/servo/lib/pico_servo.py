"""
# 원본: https://github.com/sandbo00/picoservo
# 변형 내용
  - 상수 정의: 1도마다의 값
    -> DEG_PER_1
  - 우측 중간을 0도, 좌측 중간을 180도로 할당하여 각도로 서보모터가 움직이도록 method 추가
    -> angleCcw(<각도>)
"""
from machine import Pin, PWM

class Servo:
    """ A simple class for controlling a 9g servo with the Raspberry Pi Pico.
    Attributes:
        minVal: An integer denoting the minimum duty value for the servo motor.
        maxVal: An integer denoting the maximum duty value for the servo motor.
    """
    DEG_PER_1 = 1024 / 181   # append

    def __init__(self, pin: int or Pin or PWM, minVal=2500, maxVal=7500):
        """ Creates a new Servo Object.
        args:
            pin (int or machine.Pin or machine.PWM): Either an integer denoting the number of the GPIO pin or an already constructed Pin or PWM object that is connected to the servo.
            minVal (int): Optional, denotes the minimum duty value to be used for this servo.
            maxVal (int): Optional, denotes the maximum duty value to be used for this servo.
        """

        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
        elif isinstance(pin, PWM):
            self.__pwm = pin
        self.__pwm.freq(50)
        self.minVal = minVal
        self.maxVal = maxVal

    def deinit(self):
        """ Deinitializes the underlying PWM object.
        """
        self.__pwm.deinit()

    def goto(self, value: int):
        """ Moves the servo to the specified position.
        args:
            value (int): The position to move to, represented by a value from 0 to 1024 (inclusive).
        """
        if value < 0:
            value = 0
        if value > 1024:
            value = 1024
        delta = self.maxVal-self.minVal
        target = int(self.minVal + ((value / 1024) * delta))
        self.__pwm.duty_u16(target)

    # append
    def angleCcw(self, angle):
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180

        val = int(angle * self.DEG_PER_1)
        self.goto(val)

    def middle(self):
        """ Moves the servo to the middle.
        """
        self.goto(512)

    def free(self):
        """ Allows the servo to be moved freely.
        """
        self.__pwm.duty_u16(0)
