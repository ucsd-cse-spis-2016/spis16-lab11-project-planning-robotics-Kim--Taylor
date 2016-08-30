import RPi.GPIO as GPIO
import plaympg123
BtnPin = 22

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    state = 0 #state 0 = pause and state 1 = play
    button = GPIO.input(BtnPin)
    while True:
        if button== 0 and state == 0:
            playsong()
            state = 1
        elif button== 0 and state== 1:
            pause music
            state = 0 
