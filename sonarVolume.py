import RPi.GPIO as GPIO, time
import sonar

GPIO.setmode(GPIO.BOARD)

#change volume if distance is in between ranges
def changeVol():
    distance = getDistance(echoPin= 16, trigPin= 18)
    volume = volumeLevel(distance)
    
    

#this function returns the volume level given the distance
#level 1 is highest volume and level 5 = no music
def volumeLevel(distance):
    if distance <= 2.65:
        return 1
    if distance <= 6.57:
         return 2
    if distance <= 11.42:
        return 3
    if distance <= 16.13:
        return 4
    else:
        return 5 
    
