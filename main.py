import network
import urequests
import random
from time import sleep

#Network Initialization
ssid = "xxxxxx"
password = "xxxxxx"

def ConnectWiFi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

#Connect to Network
ip = ConnectWiFi()

#ThingSpeak Initialization
server = "http://api.thingspeak.com/"
apikey = "xxxxxx"
field = 1

