import Adafruit_DHT
import time
import RPi.GPIO as GPIO
sensor = Adafruit_DHT.DHT11
dht_11 = 4 #dht11 sensor pin
def dht11():
    humi, temp=Adafruit_DHT.read_retry(sensor, dht_11)
    print("Temperature = {0:0.1f}*C Humidity={1:0.1f}%".format(temp, humi))
    time.sleep(1)
