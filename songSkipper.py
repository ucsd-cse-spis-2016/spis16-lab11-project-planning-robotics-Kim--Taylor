import RPi.GPIO as GPIO
import time

#set up the pins

sensor = 12
value = 0
tot_songs =6


GPIO.setwarnings(False)
def setup():
        ''' One time set up configurations'''
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(sensor, GPIO.IN)
        '''for pin in pins.values():
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)'''
        

'''def reset():
        for pin in pins.values():
                GPIO.output(pin, GPIO.LOW)'''      

'''def loop():
        state = 0
        while True:
                # This code repeats forever
                if state == 0:
                    time.sleep(1)
                        
                if state == 1:
                    time.sleep(1)

                if state == 2:
                    time.sleep(1)

                if state == 3:
                    reset()    
                    time.sleep(1)

                if state == 4:
                    time.sleep(1)

                if state == 5:
                    time.sleep(1)

                if state == 6:
                    time.sleep(1)
                    state = 0
                state += 1'''

def touchSensor():
        state= 0
        songnum= 0
        while True:
                #print GPIO.input(sensor)
                if state== 0 and GPIO.input(sensor)== False:
                        state=1
                elif state== 1 and GPIO.input(sensor)==True:
                        state=0
                        songnum = (songnum + 1) % tot_songs
                        print 'skipping to song ', songnum
                


                
                
def destroy():
        GPIO.cleanup()                     

if __name__ == '__main__':     # Program start from here
        setup()
        try:
                touchSensor()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                
                destroy()



