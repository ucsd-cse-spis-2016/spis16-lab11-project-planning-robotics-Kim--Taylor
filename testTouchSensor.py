import RPi.GPIO as GPIO
import time

sensor = 12
value = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
while True:
      print GPIO.input(sensor)
