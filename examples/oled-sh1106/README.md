# OLED 예제

1. Pin map

   PICO | OLED
   -----|-----
   Vcc | 3.3v OUT
   GND | GND
   SCL | I2C0 SCL (GP9)
   SDA | I2C0 SDA (GP8)

2. Driver file
   * /lib/sh1106.py

3. 예제 파일
   1. oled_raspipico_logo_sh1106.y

      ![라즈베리파이 로고와 Pico 글자 표시](images/oled_raspipico_logo_sh0116.jpg)

   2. oled_welcome_sh1106.py
      
      ![Welcome 메시지 표시](./images/oled_welcome_sh0116.jpg)
