import RPi.GPIO as GPIO
import time
from datetime import date
PIR = 21

GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

count = 1 
try:
    #time.sleep(2)
    
    while True:
        if GPIO.input(PIR) == 1:
            today = date.today()
            print("Motion Detected event #: ", count)
            count = count + 1
            print("Today's date: ", today)
            timeday = time.strftime("%H:%M:%S")
            print("Time: ", timeday)
            print("----------------------------------------------")
            time.sleep(1)
        else:
            #print("No motion detected")
            time.sleep(1)

            
except KeyboardInterrupt:
    GPIO.cleanup()
