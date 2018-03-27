#!/user/bin/python

import sys
import Adafruit_DHT


class RoomStats:

    def __init__(self, interval=1):
        self.interval = interval
        self.data = []
    
    def fetch_DHT(self):
        humidity, temp = Adafruit_DHT.read_retry(11, 4)
        temp = temp * 1.8 + 32
        return temp, humidity

    def collect(self):
        while True: 
            t, h = fetch_DHT()
            print_reading(t, h)
            self.data.append({temperature: t, humidity: h}) 

    def print_reading(temperature, humidity):
        print '{0:.1f} F, {1:.1f} %'.format(temperature, humidity)


def main():
    cred = credentials.Certificate('./.credentials.json')
    default_app = firebase_admin.initialize_app(cred)

    RoomStats().collect()

if __name__ == '__main__':
    main()
