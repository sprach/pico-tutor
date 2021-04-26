# LCD 출력 테스트

1. Pin map

   PICO | LCD
   -----|-----
   VBUS | Vcc
   GND | GND
   I2C0 SCL (GP9) | SCL 
   I2C0 SDA (GP8) | SDA

2. 예제 파일
   1. blink_loop.py
      * 루프 내에서 LED On/Off 처리하므로 루프를 빠져 나오기 전까지 다른 작업을 할 수 없음

   2. blink_callback.py
      * Timer의 내부 인터럽트 사용으로 초기 호출후 바로 종료되어도 계속 LED On/Off가 진행됨
      * 중지를 하려면 Thonny에서 강제로 'STOP' 버튼을 눌러서 프로세스를 재시작해야 함
