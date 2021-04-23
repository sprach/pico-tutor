# Raspberry Pi Pico tutorial

## lib files
* 예제에 필요한 드라이버나 패키지는 /lib 디렉토리에 알맞는 파일을 복사해 넣어야 한다.
  * 예시: examples/oled-sh1106 의 예제를 Pico 폴더에 복사해 넣을 때의 디렉토리와 파일 구조
    <pre><code>/lib/sh1106.py
    /oled_raspipico_logo_sh1106.y
    /oled_welcome_sh1106.py
    </code></pre>
    * OLED 예시의 드라이버는 sh1106.py 이므로 /lib 디렉토리에 sh1106.py 를 복사해 넣는다.

## Examples

### OLED
1. Driver: /lib/sh1106.py
2. 예제 파일
   1. oled_raspipico_logo_sh1106.y
      * 라즈베리파이 로고와 Pico 글자 표시
   2. oled_welcome_sh1106.py
      * Welcome 메시지 표시
