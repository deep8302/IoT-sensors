import time
import sys
import Adafruit_DHT
while (True):
    humidity,temperature=Adafruit_DHT.read_retry(11,4)
    print('TEMPERATURE: {0:0.1f}C HUMIDITY: {1:0.1F}%'.format(temperature,humidity))
    time.sleep(1)
    
