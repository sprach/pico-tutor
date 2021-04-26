# Raspberry Pi Pico tutorial

## lib files
* 예제에 필요한 드라이버나 패키지는 /lib 디렉토리에 알맞는 파일을 복사해 넣어야 한다.
  * 예시: examples/oled-sh1106 의 예제를 Pico 폴더에 복사해 넣을 때의 디렉토리와 파일 구조
    * Lib file(s)
    <pre><code>/lib/sh1106.py</code></pre>
    
    * Exec. files
    <pre><code>/oled_raspipico_logo_sh1106.y
    /oled_welcome_sh1106.py
    </code></pre>

## Examples

1. led (내장)
   1. blink_loop.py
   2. blink_callback.py

2. oled (sh1106)
   1. oled_raspipico_logo_sh1106.py
   2. oled_welcome_sh1106.py

3. lcd
   1. lcd_i2c_test.py

## Kits

1. Hydroponics-1
   * 아두이노용 수경재배키트를 Pico용으로 변환
