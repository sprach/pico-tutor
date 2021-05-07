# 서보 모터 예제

## Pin map

PICO | SERVO | 비고
-----|-------|-----
VBUS | 적색 | 5V
GND | 갈색 | GND
GP15 | 주황색 | Data

## Datasheet
![Pico pinout](../../docs/datasheets/microservo-sg90_datasheet.jpg)

## Driver file
* /lib/pico_servo.py
   
## 예제 파일
* PWM: PWM.duty_ns() 사용
  1. servo_dutyns_test1.py
  2. servo_dutyns_test2.py

* Servo 클래스 (/lib/pico_servo.py)
  1. servo_test1.py
     * Servo.goto()로 0~1024 사이의 값으로 서보 모터 각도 조정
  2. servo_test2.py
     * Servo.angleCcw()로 0도~180도 사이의 값으로 서보 모터 각도 조정
  3. servo_test.py
     * Servo.angleCcw()로 0도~180도 사이의 값으로 서보 모터 각도 조정

## 데이터시트상 동작 정리

## 특이사항
