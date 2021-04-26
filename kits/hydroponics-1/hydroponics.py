"""
2021.03.20. Sat by jrkim
Raspberry Pi PICO로 다두이노 수경재배 키트용 코드 변환 
"""
from time import sleep_ms
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
# https://github.com/ikornaselur/pico-dht11
from dht import DHT11, InvalidChecksum
from hydro_sensors import HydroSensors

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27
I2C_NUMBER = 0
I2C_SDA = 8
I2C_SCL = 9
DHT_GP = 19
BUZZER_GP = 20
WATER_GP = 21
LCD_ROW_SIZE = 2
LCD_COL_SIZE = 16

if __name__ == "__main__":
    print("Running test")

    i2c = I2C(I2C_NUMBER, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL))
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, LCD_ROW_SIZE, LCD_COL_SIZE)
    lcd.clear()

    hydro = HydroSensors(DHT_GP, BUZZER_GP, WATER_GP)
    
    lcd.move_to(0, 0)
    lcd.putstr("Welcome to\n  Hydroponics!")
    sleep_ms(3000)
    lcd.clear()
    
    while True:
        temp, humi, water = hydro.get_values()

        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Temp:%dC" % temp)
        lcd.putstr(",Humi:%d%%\n" % humi)

        lcd.move_to(4, 1)
        lcd.putstr("Water:%s" % ("O" if water == 1 else "X"))
    
        if water == 0:
            print("물 없수")
            hydro.set_buzzer_value(1)
            sleep_ms(100)
            hydro.set_buzzer_value(0)
            sleep_ms(100)
            hydro.set_buzzer_value(1)
            sleep_ms(100)
            hydro.set_buzzer_value(0)
            sleep_ms(100)

        sleep_ms(2000)
