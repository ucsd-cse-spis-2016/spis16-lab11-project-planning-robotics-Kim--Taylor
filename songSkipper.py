import RPi.GPIO as GPIO
import time
import playmusic
import os
from time import sleep
import subprocess

#set up the pins

sensor = 12
value = 0
tot_songs =6


GPIO.setwarnings(False)
def setup():
        ''' One time set up configurations'''
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(sensor, GPIO.IN)

def touchSensor(file_list):
        state= 0
        songnum= 0
        playsong(file_list[0])
        while True:
                #print GPIO.input(sensor)
                if state== 0 and GPIO.input(sensor)== False:
                        state=1
                elif state== 1 and GPIO.input(sensor)==True:
                        state=0
                        songnum = (songnum + 1) % tot_songs
                        print 'skipping to song ', songnum
                        quitmusic()
                        playsong(file_list[songnum])
        quitmusic() 
                

def list_files(mypath):
    file_list =[]
    for f in os.listdir(mypath):
        if os.path.isfile(os.path.join(mypath, f)):
            file_list.append(f)

    return file_list

def quitmusic():
        sleep(1)
        print "Pause track"
        subprocess.call(['killall', 'mpg123'])

def playsong(file_name):
    print file_name
    subprocess.Popen(['mpg123',file_name])
    print "Playing .....", file_name
    print "Duration "

        
                
def destroy():
        GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
        setup()
        path = "/media/USB DISK/"
        os.chdir(path)
        file_list = list_files('./')
        print file_list
        try:
                touchSensor(file_list)
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                
                destroy()
                subprocess.call(['killall', 'mpg123'])



