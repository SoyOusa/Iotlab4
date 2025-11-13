import network, time
from umqtt.simple import MQTTClient
from machine import Pin, I2C
from bmp280 import BMP280  # Make sure bmp280.py is uploaded

# Wi-Fi and MQTT setup
SSID = "Robotic WIFI"
PASSWORD = "rbtWIFI@2025"
BROKER = "test.mosquitto.org"
PORT = 1883
CLIENT_ID = b"esp32_bmp280"
TOPIC = b"/aupp/morning/OU"
KEEPALIVE = 30

# BMP280 setup
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
bmp = BMP280(i2c)

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(0.3)
    print("WiFi Connected:", wlan.ifconfig())

def make_client():
    return MQTTClient(client_id=CLIENT_ID, server=BROKER, port=PORT, keepalive=KEEPALIVE)

def main():
    wifi_connect()
    client = make_client()
    client.connect()
    print("MQTT connected")

    while True:
        temperature = bmp.temperature
        pressure = bmp.pressure
        altitude = bmp.altitude
        msg = '{{"temperature": {:.2f}, "pressure": {:.2f}, "altitude": {:.2f}}}'.format(temperature, pressure, altitude)
        client.publish(TOPIC, msg)
        print("Published:", msg)
        time.sleep(5)

main()
