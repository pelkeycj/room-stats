#!/user/bin/python

import sys
import Adafruit_DHT
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

def main():
    GPIO.setwarnings(False)
    lcd = init_lcd() 

    while True:
        humid, temp = Adafruit_DHT.read_retry(11, 4)
        temp = to_fahrenheit(temp)
        write_lcd(lcd, temp, humid)

def init_lcd():
    ''' Create the LCD with BCM pin numberings 
        NOTE: correct pin values must be used '''
    return CharLCD(pin_rs=22, pin_rw=24, pin_e=23, pins_data=[9, 25, 11, 8], numbering_mode=GPIO.BCM)

def write_lcd(lcd, temp, humid):
    lcd.clear()
    lcd.write_string("Temp:     {0:.1f}F".format(temp))
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: {0:.1f}%".format(humid))

def to_fahrenheit(temp):
    return temp*1.8 + 32

if __name__ == '__main__':
    main()
