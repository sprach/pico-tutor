# 수경재배 #1

1. 개요
   * 다우블록의 아두이노 수경재배 키트 기준
   * 초기 버전으로 lib 디렉토리없음

2. Pin maps
   1. LCD

      PICO | LCD
      -----|-----
      VBUS | Vcc
      GND | GND
      I2C0 SCL (GP9) | SCL 
      I2C0 SDA (GP8) | SDA

   2. 온습도 (DHT11)

      PICO | DHT11
      -----|-----
      3.3v OUT | Vcc
      GND | GND
      GP19 | DATA

   3. 비접촉 수위 센서 (XKC-Y26-NPN)

      PICO | WATER
      -----|-----
      3.3v OUT | + 
      GND | -
      GP21 | S

   4. 부저 (Piezo)

      PICO | BUZZER
      -----|-----
      3.3v OUT | + 
      GND | -
      GP20 | S

3. Driver files
   * dht.py : 온습도
   * lcd_api.py : LCD (Base, esp8266 변형)
   * pico_i2c_lcd.py: LCD
   * hydro_sensors.py: 센서 처리 모음. 온습도, 부저, 수위

4. 실행 파일: hydroponics.py
