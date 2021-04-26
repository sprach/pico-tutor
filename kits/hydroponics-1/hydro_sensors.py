"""
2021.03.20. Sat by jrkim
Raspberry Pi PICO로 다두이노 수경재배 키트용 코드 변환 
"""
from machine import Pin

class HydroSensors:
    def __init__(self, dht_gp, buz_gp, water_gp):
        dht_pin = Pin(dht_gp, Pin.OUT, Pin.PULL_DOWN)
        self.dht = DHT11(dht_pin)

        self.buz_pin = Pin(buz_gp, Pin.OUT)
        self.water_check_pin = Pin(water_gp, Pin.IN, Pin.PULL_DOWN)
    
    def get_values(self):
        try:
            temp = self.dht.temperature
            humi = self.dht.humidity
        except InvalidChecksum:
            temp = -1
            humi = -1
        
        water = self.water_check_pin.value()
        
        return temp, humi, water
    
    def set_buzzer_value(self, val):
        self.buz_pin.value(val)
